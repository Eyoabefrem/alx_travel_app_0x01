#!/usr/bin/env python3
"""
Database models for listings app including Listing, Booking, and Review.

Defines fields, relationships, and constraints as per specifications.
"""

from django.db import models

class Listing(models.Model):
    """
    Model representing a property listing.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    host = models.ForeignKey(
        "auth.User",  # assuming default User model
        on_delete=models.CASCADE,
        related_name="listings"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """
    Model representing a booking for a listing by a user.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user} for {self.listing}"


class Review(models.Model):
    """
    Model representing a review of a listing by a user.
    """
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} for {self.listing}"
