#!/usr/bin/env python3
"""
Management command to seed the database with sample listings.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # Create a sample user if none exists
        user, created = User.objects.get_or_create(
            username="hostuser",
            defaults={"email": "host@example.com", "password": "hostpass"}
        )

        if created:
            user.set_password("hostpass")
            user.save()

        listings = [
            {
                "title": "Cozy Cottage",
                "description": "A cozy cottage in the countryside.",
                "address": "123 Country Lane",
                "price_per_night": 100.00,
            },
            {
                "title": "Beachfront Villa",
                "description": "Luxurious villa with beach access.",
                "address": "456 Ocean Drive",
                "price_per_night": 250.00,
            },
            {
                "title": "Downtown Apartment",
                "description": "Modern apartment in downtown.",
                "address": "789 City Blvd",
                "price_per_night": 150.00,
            },
        ]

        for data in listings:
            listing, created = Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "address": data["address"],
                    "price_per_night": data["price_per_night"],
                    "host": user
                }
            )
            if created:
                self.stdout.write(f"Created listing: {listing.title}")
            else:
                self.stdout.write(f"Listing already exists: {listing.title}")

        self.stdout.write("Seeding complete.")
