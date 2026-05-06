---
aid: carsxe
name: CarsXE
description: CarsXE is a comprehensive vehicle data API platform offering VIN decoding, vehicle specifications, market value estimates, vehicle history, vehicle imagery, license plate recognition, OBD fault-code decoding, international VIN decoding, and recall lookups. Designed for automotive marketplaces, dealerships, insurance, lending, fleet, and claims platforms that need programmatic access to rich, current vehicle data.
type: Index
position: Provider
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automotive
  - Vehicles
  - VIN
  - Vehicle Data
  - License Plate
  - OCR
  - Automobiles
created: '2025-02-24'
modified: '2026-04-23'
url: https://raw.githubusercontent.com/api-evangelist/carsxe/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: carsxe:vehicle-specifications-api
    name: CarsXE Vehicle Specifications API
    description: VIN decoding and comprehensive vehicle specification lookup. Returns year, make, model, trim, engine, drivetrain, body style, and detailed feature and option data for a given North American VIN.
    humanURL: https://api.carsxe.com/vehicle-specifications
    baseURL: https://api.carsxe.com
    tags:
      - VIN Decoder
      - Specifications
      - Vehicle Data
    properties:
      - type: Documentation
        url: https://api.carsxe.com/vehicle-specifications
  - aid: carsxe:vehicle-market-value-api
    name: CarsXE Vehicle Market Value API
    description: Returns market value estimates (retail, wholesale, trade-in) for new and used vehicles by VIN, informed by millions of historical vehicle sales.
    humanURL: https://api.carsxe.com/vehicle-market-value
    baseURL: https://api.carsxe.com
    tags:
      - Market Value
      - Pricing
      - Valuation
    properties:
      - type: Documentation
        url: https://api.carsxe.com/vehicle-market-value
  - aid: carsxe:vehicle-images-api
    name: CarsXE Vehicle Images API
    description: Retrieves high-quality photos of vehicles by year, make, model (and optional trim / color / background-transparency options) for use in marketplaces, dealer sites, and comparison tools.
    humanURL: https://api.carsxe.com/vehicle-images
    baseURL: https://api.carsxe.com
    tags:
      - Images
      - Media
      - Vehicle Data
    properties:
      - type: Documentation
        url: https://api.carsxe.com/vehicle-images
  - aid: carsxe:vin-ocr-api
    name: CarsXE VIN OCR API
    description: OCR endpoint that extracts a VIN string from an image of a VIN plate, windshield, or document, enabling mobile-first vehicle-onboarding and inspection workflows.
    humanURL: https://api.carsxe.com/vin-ocr
    baseURL: https://api.carsxe.com
    tags:
      - OCR
      - VIN
      - AI
    properties:
      - type: Documentation
        url: https://api.carsxe.com/vin-ocr
  - aid: carsxe:vehicle-plate-decoder-api
    name: CarsXE Vehicle Plate Decoder API
    description: Decodes vehicle information from a license plate plus state/province, returning make, model, year, and VIN where available.
    humanURL: https://api.carsxe.com/vehicle-plate-decoder
    baseURL: https://api.carsxe.com
    tags:
      - License Plate
      - Lookup
      - Vehicle Data
    properties:
      - type: Documentation
        url: https://api.carsxe.com/vehicle-plate-decoder
  - aid: carsxe:vehicle-plate-recognition-api
    name: CarsXE Vehicle Plate Recognition API
    description: Image-to-text OCR for license plates. Paired with the Plate Decoder, enables full vehicle lookup starting from a plate image, supporting parking, access-control, law-enforcement, and valet use cases.
    humanURL: https://api.carsxe.com/vehicle-plate-recognition
    baseURL: https://api.carsxe.com
    tags:
      - License Plate
      - OCR
      - AI
    properties:
      - type: Documentation
        url: https://api.carsxe.com/vehicle-plate-recognition
  - aid: carsxe:vehicle-history-api
    name: CarsXE Vehicle History API
    description: Raw vehicle-history data endpoint returning title records, accident history, odometer readings, service history, and salvage/lemon flags for a given VIN.
    humanURL: https://api.carsxe.com/vehicle-history
    baseURL: https://api.carsxe.com
    tags:
      - History
      - Title
      - Accident
    properties:
      - type: Documentation
        url: https://api.carsxe.com/vehicle-history
  - aid: carsxe:vehicle-recalls-api
    name: CarsXE Vehicle Recalls API
    description: Returns safety-recall and campaign data for a given VIN, sourced from manufacturer and NHTSA data, for use in inspection, compliance, and pre-purchase workflows.
    humanURL: https://api.carsxe.com/vehicle-recalls
    baseURL: https://api.carsxe.com
    tags:
      - Recalls
      - Safety
      - Compliance
    properties:
      - type: Documentation
        url: https://api.carsxe.com/vehicle-recalls
  - aid: carsxe:international-vin-decoder-api
    name: CarsXE International VIN Decoder API
    description: VIN decoding for non-US vehicles, returning make, model, year, and market-specific trim/spec data for international markets.
    humanURL: https://api.carsxe.com/international-vin-decoder
    baseURL: https://api.carsxe.com
    tags:
      - VIN Decoder
      - International
      - Specifications
    properties:
      - type: Documentation
        url: https://api.carsxe.com/international-vin-decoder
  - aid: carsxe:obd-codes-decoder-api
    name: CarsXE OBD Codes Decoder API
    description: Matches an OBD-II diagnostic trouble code (DTC) to a human-readable vehicle fault description for use in service, maintenance, and connected-car applications.
    humanURL: https://api.carsxe.com/obd-codes-decoder
    baseURL: https://api.carsxe.com
    tags:
      - OBD
      - Diagnostics
      - Maintenance
    properties:
      - type: Documentation
        url: https://api.carsxe.com/obd-codes-decoder
common:
  - type: Website
    url: https://api.carsxe.com/
  - type: Portal
    name: Vehicle Data API | CarsXE
    url: https://api.carsxe.com/
  - type: Documentation
    url: https://api.carsxe.com/docs
  - type: GettingStarted
    url: https://api.carsxe.com/docs/quickstart
  - type: Authentication
    url: https://api.carsxe.com/docs/authentication
  - type: Errors
    url: https://api.carsxe.com/docs/errors
  - type: Pricing
    url: https://api.carsxe.com/pricing
  - type: About
    url: https://api.carsxe.com/about
  - type: Blog
    url: https://api.carsxe.com/blog
  - type: Support
    url: https://api.carsxe.com/support
  - type: Contact
    url: https://api.carsxe.com/contact-us
  - type: TermsOfService
    url: https://api.carsxe.com/terms-and-conditions
  - type: Login
    url: https://api.carsxe.com/login
  - type: SignUp
    url: https://api.carsxe.com/register
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
