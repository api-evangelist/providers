---
aid: autopay
name: Autopay
description: Autopay is a Norwegian parking payment and management platform that provides APIs for parking operators, landlords, fleet managers, and third-party integrators. The platform enables automated parking permit management, payment processing, fleet tracking, and parking statistics with 13+ distinct API endpoints. All integrators must accept the Autopay API Usage Agreement before accessing the APIs.
tags:
  - Parking
  - Parking Payments
  - Fleet Management
  - Permits
  - Parking Operators
  - Norway
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-08'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/autopay/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: autopay:accounting-api
    name: Autopay Accounting API
    description: The Autopay Accounting API provides Autopay invoicing data to external accounting and ERP systems, enabling automated reconciliation of parking revenue and invoice export.
    humanURL: https://developer.autopay.io
    tags:
      - Accounting
      - Invoicing
      - Finance
    properties:
      - type: Documentation
        url: https://developer.autopay.io
      - type: Authentication
        url: https://developer.autopay.io
  - aid: autopay:booking-api
    name: Autopay Booking API
    description: The Autopay Booking API enables assignment of anonymous parking permits to vehicles, supporting short-term and pre-booked parking allocations in managed parking facilities.
    humanURL: https://developer.autopay.io
    tags:
      - Booking
      - Parking Permits
      - Reservations
    properties:
      - type: Documentation
        url: https://developer.autopay.io
  - aid: autopay:parking-api
    name: Autopay Parking API
    description: The Autopay Parking API handles zone entry notifications and parking session modifications, enabling integration with parking gate systems, sensors, and barrier control equipment to track vehicle arrivals and departures in parking zones.
    humanURL: https://developer.autopay.io
    tags:
      - Parking Sessions
      - Zone Entry
      - Gate Control
    properties:
      - type: Documentation
        url: https://developer.autopay.io
  - aid: autopay:payment-api
    name: Autopay Payment API
    description: The Autopay Payment API enables third-party systems to take payment responsibility for parking sessions, supporting employer-paid parking, fleet-billed parking, and visitor parking validation workflows.
    humanURL: https://developer.autopay.io
    tags:
      - Payments
      - Parking Payment
      - Third-Party Billing
    properties:
      - type: Documentation
        url: https://developer.autopay.io
  - aid: autopay:permit-tenant-api
    name: Autopay Permit Tenant API
    description: The Autopay Permit Tenant API enables tenants in managed properties to manage their parking permits, including adding vehicles, modifying permit allocations, and tracking permit usage within their assigned quota.
    humanURL: https://developer.autopay.io
    tags:
      - Permits
      - Tenant Management
      - Vehicle Permits
    properties:
      - type: Documentation
        url: https://developer.autopay.io
  - aid: autopay:fleet-api
    name: Autopay Fleet API
    description: The Autopay Fleet API provides fleet information for company vehicle fleets, enabling fleet managers to track vehicle parking activity, costs, and permit usage across all fleet vehicles.
    humanURL: https://developer.autopay.io
    tags:
      - Fleet Management
      - Vehicle Tracking
      - Corporate Parking
    properties:
      - type: Documentation
        url: https://developer.autopay.io
  - aid: autopay:statistics-api
    name: Autopay Statistics API
    description: The Autopay Statistics API exports parking statistics for operators and landlords, providing data on occupancy rates, revenue, session volumes, and permit utilization for parking facility management and reporting.
    humanURL: https://developer.autopay.io
    tags:
      - Analytics
      - Statistics
      - Reporting
      - Occupancy
    properties:
      - type: Documentation
        url: https://developer.autopay.io
  - aid: autopay:vehicle-api
    name: Autopay Vehicle API
    description: The Autopay Vehicle API fetches data about a vehicle in a specific parking zone, providing real-time information on vehicle presence, active session status, and permit validity for enforcement and access control purposes.
    humanURL: https://developer.autopay.io
    tags:
      - Vehicle Data
      - Zone Status
      - Enforcement
    properties:
      - type: Documentation
        url: https://developer.autopay.io
  - aid: autopay:tap-park-api
    name: Autopay Tap and Park API
    description: The Autopay Tap and Park API enables third-party applications to validate parking sessions in Autopay-managed zones, supporting contactless parking validation via NFC, mobile apps, or access control systems.
    humanURL: https://developer.autopay.io
    tags:
      - Parking Validation
      - NFC
      - Mobile Payments
      - Contactless
    properties:
      - type: Documentation
        url: https://developer.autopay.io
common:
  - type: Portal
    url: https://developer.autopay.io
  - type: Website
    url: https://autopay.no
  - type: Documentation
    url: https://developer.autopay.io
  - type: Authentication
    url: https://developer.autopay.io
  - type: TermsOfService
    url: https://developer.autopay.io
  - type: Features
    data:
      - name: OAuth Authentication
        description: All Autopay APIs use OAuth for secure authentication and authorization. Integrators must obtain API credentials and accept the Usage Agreement before accessing production endpoints.
      - name: Permit Management
        description: Comprehensive parking permit lifecycle management for landlords, operators, and tenants including allocation, assignment, modification, and expiration.
      - name: Real-Time Zone Status
        description: Real-time counts of active parking sessions in parking zones via the Status API, enabling dynamic pricing and occupancy monitoring.
      - name: Fleet Parking Integration
        description: Corporate fleet parking management with automatic billing to fleet accounts and vehicle-level tracking across parking facilities.
      - name: Parking Validation
        description: Tap and Park API for third-party validation of parking sessions in Autopay zones, supporting retail validation, employer programs, and visitor parking workflows.
  - type: UseCases
    data:
      - name: Property Parking Management
        description: Landlords manage tenant parking permits and allocations through the Permit Landlord and Tenant APIs for residential and commercial properties.
      - name: Corporate Fleet Parking
        description: Companies manage fleet vehicle parking costs and permits using the Fleet API with automatic billing to corporate accounts.
      - name: Parking Revenue Reporting
        description: Parking operators export revenue and occupancy statistics from the Statistics API into accounting and BI systems for reporting.
      - name: Visitor Parking Validation
        description: Retail, hospitality, and office tenants validate visitor parking through the Tap and Park API integrated with access control or POS systems.
  - type: Integrations
    data:
      - name: Accounting Systems
        description: Export Autopay invoicing data to external ERP and accounting systems via the Accounting API for automated reconciliation.
      - name: Building Access Control
        description: Integration with building access control and gate systems via the Parking API for automated entry/exit tracking.
      - name: Fleet Management Platforms
        description: Connect corporate fleet management software with Autopay for parking cost tracking and vehicle permit assignment.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
