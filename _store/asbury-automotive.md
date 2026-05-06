---
aid: asbury-automotive
url: https://raw.githubusercontent.com/api-evangelist/asbury-automotive/refs/heads/main/apis.yml
name: Asbury Automotive Group
tags:
  - Automotive
  - Dealerships
  - Retail
  - Vehicles
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-19'
description: Asbury Automotive Group is one of the largest automotive retailers in the United States, operating new and used vehicle dealerships across multiple states and brands. Headquartered in Duluth, Georgia, Asbury operates approximately 200 dealerships representing 30+ automotive brands including luxury and non-luxury vehicles. The company operates under multiple brand names including Coggin Automotive Group, Crown Automotive Group, Park Place Dealerships, Nalley Automotive Group, and others. Asbury does not expose a public developer API but operates digital retail platforms including Clicklane, their proprietary online vehicle purchase platform.
apis:
  - aid: asbury-automotive:clicklane-platform
    name: Asbury Automotive Clicklane Platform
    description: Clicklane is Asbury Automotive's proprietary online vehicle purchase platform that enables customers to complete the full car buying process digitally, including vehicle selection, financing, trade-in valuation, F&I products, and final purchase without visiting a dealership.
    humanURL: https://www.clicklane.com/
    baseURL: https://www.clicklane.com
    tags:
      - Automotive
      - Digital Retail
      - Vehicle Purchase
      - E-Commerce
    properties:
      - type: Documentation
        url: https://www.clicklane.com/
common:
  - type: Portal
    url: https://www.asburyauto.com/
    title: Asbury Automotive Group Website
  - type: Features
    data:
      - name: Clicklane Digital Retail
        description: Proprietary online vehicle purchase platform allowing customers to complete the entire car buying process digitally including financing, trade-ins, and F&I products.
      - name: Multi-Brand Dealership Network
        description: Operates approximately 200 dealerships across 30+ automotive brands including luxury brands (Lexus, Mercedes, BMW, Audi) and non-luxury (Toyota, Honda, Ford, Chevrolet).
      - name: Digital Service Scheduling
        description: Online service appointment scheduling across all Asbury dealership brands through brand-specific and aggregated scheduling tools.
  - type: UseCases
    data:
      - name: Digital Vehicle Purchase
        description: Customers use Clicklane to research, finance, and purchase vehicles entirely online without visiting a dealership.
      - name: Trade-In Valuation
        description: Vehicle owners use Asbury's digital tools to obtain trade-in valuations for their current vehicles as part of new vehicle purchase.
      - name: Service and Parts
        description: Vehicle owners schedule service appointments and order parts through Asbury's dealership service departments.
  - type: Integrations
    data:
      - name: OEM Dealer Management Systems
        description: Asbury integrates with manufacturer dealer management systems and DMS platforms like CDK Global and Reynolds & Reynolds.
      - name: Finance and Insurance Partners
        description: Integration with lenders and F&I product providers through Asbury's F&I technology platform across all dealership locations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
