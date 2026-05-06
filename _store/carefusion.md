---
aid: carefusion
url: https://raw.githubusercontent.com/api-evangelist/carefusion/refs/heads/main/apis.yml
name: CareFusion (BD)
description: CareFusion is a medical technology brand, acquired by BD (Becton, Dickinson and Company) in 2015, best known for the Alaris infusion system and the Pyxis automated dispensing product line. CareFusion does not expose a public developer API; instead, its devices and dispensing systems interoperate with hospital EMRs and pharmacy systems over HL7 v2 messaging, smart-pump interoperability middleware, and vendor-managed integration services. The Alaris Infusion Interoperability program wirelessly transmits orders from EMRs (such as Epic and Cerner) into Alaris large-volume and syringe modules and returns infusion status back to the EMR in near real time, using the Alaris Guardrails drug library as a safety layer.
type: Index
x-type: company
position: Consumer
access: Partner
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automated Dispensing
  - BD
  - CareFusion
  - Connected Devices
  - EMR Integration
  - Healthcare
  - HL7
  - Infusion Pumps
  - Medical Devices
  - Pyxis
  - Smart Pumps
created: '2026-03-23'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: carefusion:alaris-infusion-interoperability
    name: Alaris Infusion Interoperability
    description: The Alaris Infusion Interoperability solution connects the Alaris System (large-volume pump modules and syringe modules) to hospital EMR platforms so that physician infusion orders flow wirelessly into pumps and live infusion status is returned to the EMR. The integration is delivered through BD's infusion interoperability middleware and is typically deployed with Epic and Cerner EMRs using HL7 v2 messaging. The Alaris Guardrails drug library provides the clinical decision support and safety layer that validates dose, concentration, and delivery parameters before a pump accepts an order.
    humanURL: https://www.bd.com/en-us/products-and-solutions/products/product-families/alaris-infusion-system
    tags:
      - EMR Integration
      - HL7
      - Infusion Pumps
      - Medical Devices
    properties:
      - url: https://www.bd.com/en-us/products-and-solutions/products/product-families/alaris-infusion-system
        type: Documentation
      - url: https://pages.carefusion.com/AlarisInteroperability.html
        type: Product
    x-features:
      - EMR-to-pump order transmission for large-volume and syringe modules
      - Near real-time infusion status returned to the EMR
      - Alaris Guardrails drug library for clinical decision support
      - HL7 v2 messaging through BD interoperability middleware
      - Epic, Cerner, and other major EMR compatibility
      - Reduces error-prone manual pump programming
      - Auto-documentation of infusion events in the patient record
    x-use-cases:
      - Closed-loop infusion pump integration with EMR
      - Nursing workflow reduction for high-volume infusions
      - Sepsis, anesthesia, and oncology infusion safety
      - Medication administration record (MAR) auto-charting
      - Infusion analytics and drug library governance
  - aid: carefusion:pyxis-automated-dispensing
    name: Pyxis Automated Dispensing Integration
    description: Pyxis MedStation and Pyxis ES automated dispensing cabinets integrate with hospital pharmacy information systems and EMRs so that medication profiles, inventory, and dispense events are synchronized. Integration is delivered through BD Pyxis interoperability services using HL7 v2 messaging (ADT, ORM, RDE, RDS) and direct pharmacy system connectors rather than a public REST API.
    humanURL: https://www.bd.com/en-us/products-and-solutions/products/product-families/bd-pyxis-medstation-es-system
    tags:
      - Automated Dispensing
      - EMR Integration
      - HL7
      - Pharmacy
      - Pyxis
    properties:
      - url: https://www.bd.com/en-us/products-and-solutions/products/product-families/bd-pyxis-medstation-es-system
        type: Documentation
    x-features:
      - Pharmacy system and EMR integration via HL7 v2
      - ADT-based patient profile synchronization
      - Medication order, dispense, and inventory messages
      - Controlled-substance diversion analytics
      - Pharmacy and unit-based cabinet configuration
    x-use-cases:
      - Nursing unit medication dispensing
      - Pharmacy inventory replenishment
      - Controlled-substance chain-of-custody
      - Drug diversion analytics and reporting
      - ADT-driven medication profile updates
common:
  - type: Website
    url: https://www.bd.com/en-us/products-and-solutions/brand-families/carefusion
  - type: Alaris Product Page
    url: https://www.bd.com/en-us/products-and-solutions/products/product-families/alaris-infusion-system
  - type: Pyxis Product Page
    url: https://www.bd.com/en-us/products-and-solutions/products/product-families/bd-pyxis-medstation-es-system
  - type: BD Corporate Site
    url: https://www.bd.com/
  - type: Contact
    url: https://www.bd.com/en-us/about-bd/contact-us
  - type: Terms of Service
    url: https://www.bd.com/en-us/terms-of-use
  - type: Privacy Policy
    url: https://www.bd.com/en-us/our-company/privacy
  - type: LinkedIn
    url: https://www.linkedin.com/company/bd1/
  - type: X
    url: https://x.com/BDandCo
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
