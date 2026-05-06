---
aid: autonation
name: AutoNation
description: AutoNation is the largest automotive retailer in the United States, operating over 250 new and used vehicle franchises along with collision centers, parts and service operations, and AutoNation USA used-vehicle stores. The company sells vehicles across most major OEM brands and provides digital retail, financing, and service scheduling capabilities through its website and mobile applications.
url: https://raw.githubusercontent.com/api-evangelist/autonation/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Automotive Retail
  - Car Dealership
  - Vehicle Sales
  - Auto Finance
  - Service Scheduling
  - Used Vehicles
apis:
  - aid: autonation:digital-retail
    name: AutoNation Digital Retail Platform
    description: AutoNation operates a digital retail platform at autonation.com that enables consumers to browse new and used vehicle inventory, configure purchases, apply for financing, and schedule vehicle deliveries online. The platform integrates dealer management systems (DMS) with online vehicle listings and CRM workflows.
    humanURL: https://www.autonation.com
    tags:
      - Digital Retail
      - Vehicle Search
      - Inventory
      - Financing
    properties:
      - type: Website
        url: https://www.autonation.com
  - aid: autonation:service-scheduling
    name: AutoNation Service Scheduling
    description: AutoNation provides online and app-based service appointment scheduling for vehicle maintenance and repairs at AutoNation dealership service centers across the United States. Customers can schedule oil changes, recalls, warranty repairs, and other automotive services.
    humanURL: https://www.autonation.com/service
    tags:
      - Service Scheduling
      - Vehicle Maintenance
      - Repair
      - Automotive Service
    properties:
      - type: Website
        url: https://www.autonation.com/service
common:
  - type: Website
    url: https://www.autonation.com
  - type: Features
    data:
      - name: Digital Vehicle Shopping
        description: Online vehicle search and purchase workflow allowing customers to browse inventory, configure deals, and complete purchases digitally without visiting a dealership.
      - name: AutoNation Finance
        description: Integrated financing platform allowing customers to apply for vehicle loans and lease programs online through AutoNation's lending partners.
      - name: Service Scheduling
        description: Online and mobile service appointment booking for AutoNation dealership service centers nationwide.
      - name: AutoNation USA
        description: Used vehicle retail stores offering one-price, no-haggle buying experience for pre-owned vehicles with digital purchase capabilities.
      - name: Collision Center Network
        description: Network of AutoNation collision centers providing auto body repair and insurance claim coordination services.
  - type: UseCases
    data:
      - name: New Vehicle Purchase
        description: Browse new vehicle inventory from major OEM brands at AutoNation dealerships and complete purchases through the digital retail platform.
      - name: Used Vehicle Acquisition
        description: Search and purchase certified pre-owned and used vehicles through AutoNation's dealership network and AutoNation USA standalone stores.
      - name: Vehicle Service Management
        description: Schedule and manage routine and warranty vehicle service appointments at AutoNation dealership service departments.
      - name: Auto Finance Application
        description: Apply for vehicle financing online and receive pre-approval decisions integrated into the vehicle purchase workflow.
  - type: Integrations
    data:
      - name: OEM Dealer Systems
        description: Integration with manufacturer dealer portals and ordering systems from Ford, GM, Toyota, BMW, Mercedes-Benz, and other OEM brands.
      - name: Dealer Management Systems
        description: Connection to DMS platforms (Reynolds and Reynolds, CDK Global) for inventory, service, and customer data management across dealerships.
      - name: AutoNation Finance Partners
        description: Integration with captive and third-party lenders for vehicle financing application routing and deal structuring.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
