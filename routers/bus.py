from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from typing import List

router = APIRouter(
    prefix="/bus",
    tags=["buses"]
)


@router.post("/", response_model=schemas.Bus, status_code=201)
def create_bus(bus: schemas.BusCreate, db: Session = Depends(get_db)):
    new_bus = models.Bus(
        route=bus.route,
        latitude=bus.latitude,
        longitude=bus.longitude
    )
    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)
    return new_bus


@router.get("/", response_model=list[schemas.Bus])
def get_all_buses(db: Session = Depends(get_db)):
    return db.query(models.Bus).all()


@router.get("/{route}", response_model=list[schemas.Bus])
def get_bus(route: str, db: Session = Depends(get_db)):
    buses = db.query(models.Bus).filter(models.Bus.route == route).all()

    if not buses:
        raise HTTPException(
            status_code=404,
            detail=f"Bus with route {route} not found"
        )

    return buses


@router.patch("/{route}/location", response_model=schemas.Bus, status_code=201)
def update_bus_location(route: str, location: schemas.BusLocationUpdate, db: Session = Depends(get_db)):
    bus = db.query(models.Bus).filter(models.Bus.route == route).first()

    if not bus:
        raise HTTPException(
            status_code=404,
            detail=f"Bus with route {route} not found"
        )

    bus.latitude = location.latitude
    bus.longitude = location.longitude

    db.commit()
    db.refresh(bus)
    return bus


@router.delete("/{route}", status_code=204)
def delete_bus(route: str, db: Session = Depends(get_db)):
    bus = db.query(models.Bus).filter(models.Bus.route == route).first()

    if not bus:
        raise HTTPException(
            status_code=404,
            detail=f"Bus with route {route} not found"
        )

    db.delete(bus)
    db.commit()
    return
