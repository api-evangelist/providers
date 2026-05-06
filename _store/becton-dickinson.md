---
aid: becton-dickinson
url: https://raw.githubusercontent.com/api-evangelist/becton-dickinson/refs/heads/main/apis.yml
name: Becton Dickinson
description: Becton Dickinson (BD) is a global medical technology company that develops, manufactures, and sells medical devices, instrument systems, and reagents. In October 2025, BD launched the BD Incada Connected Care Platform, an AI-enabled, cloud-based platform built on AWS that unifies data from nearly 3 million connected BD devices including infusion pumps, patient monitors, and pharmacy robotics. BD also produces the Pyxis medication management system and integrates with EMRs via HL7 FHIR standards for clinical data exchange.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Healthcare
  - Medical Devices
  - Infusion Therapy
  - Medication Management
  - Connected Health
  - Diagnostics
access: 3rd-Party
created: '2026-03-21'
modified: '2026-04-19'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: becton-dickinson:bd-incada-platform
    name: BD Incada Connected Care Platform
    description: The BD Incada Connected Care Platform is a scalable, AI-enabled, cloud-based platform launched in October 2025 that unifies BD device data from infusion pumps, patient monitors, and pharmacy robotics into one intelligent ecosystem. Built on AWS, it provides enterprise-wide medication inventory visibility, AI-powered natural language analytics, and integrates with major EMR systems via HL7 FHIR standards.
    humanURL: https://www.bd.com/en-us/
    tags:
      - Healthcare
      - Connected Devices
      - AI
      - Medication Management
      - EMR Integration
    properties:
      - type: Documentation
        url: https://www.bd.com/en-us/
  - aid: becton-dickinson:pyxis
    name: BD Pyxis Medication Management System
    description: BD Pyxis is a medication management and dispensing system used in hospitals to control medication access, reduce errors, and streamline pharmacy workflows. Pyxis connects to hospital information systems and EMRs for medication ordering, dispensing, and reconciliation workflows. The BD Incada platform extends Pyxis with cloud-based analytics and AI capabilities.
    humanURL: https://www.bd.com/en-us/products-and-solutions/products/product-families/pyxis
    tags:
      - Healthcare
      - Medication Management
      - Pharmacy
      - Hospital Automation
    properties:
      - type: Documentation
        url: https://www.bd.com/en-us/products-and-solutions/products/product-families/pyxis
common:
  - type: Website
    url: https://www.bd.com/
  - type: Security
    url: https://www.bd.com/en-us/company/cybersecurity
  - type: PrivacyPolicy
    url: https://www.bd.com/en-us/company/legal-notices-and-privacy/privacy
  - type: TermsOfService
    url: https://www.bd.com/en-us/company/legal-notices-and-privacy
  - type: Features
    data:
      - name: BD Incada Connected Care Platform
        description: AI-enabled cloud platform launched in 2025 that unifies data from nearly 3 million BD connected medical devices on AWS infrastructure.
      - name: AI-Powered Analytics
        description: Natural language search and AI-powered insights for medication inventory, device utilization, and clinical operational analytics.
      - name: HL7 FHIR Integration
        description: Healthcare interoperability using HL7 and FHIR standards for EMR integration with Mirth, Cloverleaf, and Rhapsody interface engines.
      - name: Medication Management
        description: Pyxis automated dispensing system with connected pharmacy workflow, medication safety, and inventory management.
      - name: Device Connectivity
        description: Connectivity for infusion pumps, vital signs monitors, and pharmacy robotics to hospital information systems.
      - name: Enterprise Analytics
        description: Customizable dashboards and analytics enabling frontline clinical teams to act on device and medication data insights.
  - type: UseCases
    data:
      - name: Medication Safety
        description: Reduce medication errors by connecting BD dispensing systems with EMR medication orders and administration verification.
      - name: Clinical Data Interoperability
        description: Enable hospital IT to integrate BD device data into clinical workflows using HL7 FHIR standards.
      - name: Pharmacy Analytics
        description: Gain enterprise-wide visibility into medication inventory, dispensing patterns, and waste reduction opportunities.
      - name: Connected Care Workflows
        description: Unify data from infusion pumps, patient monitors, and pharmacy systems to support coordinated clinical care decisions.
  - type: Integrations
    data:
      - name: Epic EMR
        description: Integration with Epic electronic medical records for medication order and administration workflow connectivity.
      - name: Cerner EMR
        description: Integration with Cerner/Oracle Health for clinical data exchange and medication management.
      - name: Mirth Connect
        description: Open-source HL7 interface engine used with BD systems for healthcare data exchange.
      - name: AWS
        description: Amazon Web Services infrastructure powering the BD Incada Connected Care Platform cloud analytics.
      - name: Cloverleaf
        description: Healthcare integration engine used with BD systems for interfacing with hospital information systems.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
