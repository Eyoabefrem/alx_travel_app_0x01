#!/usr/bin/env python3
"""
Serializers for Listing and Booking models for API representation.
"""

from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for Listing model.
    """
    class Meta:
        model = Listing
        fields = [
            "id",
            "title",
            "description",
            "address",
            "price_per_night",
            "host",
            "created_at"
        ]


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for Booking model.
    """
    class Meta:
        model = Booking
        fields = [
            "id",
            "listing",
            "user",
            "start_date",
            "end_date",
            "status",
            "created_at"
        ]
