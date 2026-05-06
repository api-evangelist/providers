---
aid: solventum
name: Solventum
description: Solventum is a Fortune 500 healthcare company spun off from 3M in 2024, focused on healthcare technology including medical-surgical solutions, dental and orthodontic products, health information systems, and purification and filtration technologies. Solventum serves hospitals, clinics, dental practices, and healthcare IT organizations worldwide.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Dental
  - EHR
  - Electronic Health Records
  - Healthcare
  - Healthcare IT
  - Health Information Systems
  - Medical Devices
  - Medical Technology
url: https://raw.githubusercontent.com/api-evangelist/solventum/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: solventum:health-information-systems
    name: Solventum Health Information Systems API
    description: Solventum's Health Information Systems (formerly 3M HIS) provides APIs for clinical documentation, coding and grouping, computer-assisted coding (CAC), revenue cycle management, and healthcare analytics. These APIs integrate with EHR systems such as Epic, Cerner, and Oracle Health to support clinical coding, DRG grouping, and quality reporting.
    humanURL: https://www.solventum.com/en-us/home/health-information-systems/
    tags:
      - CAC
      - Clinical Coding
      - DRG Grouping
      - EHR Integration
      - Health Information Systems
      - Healthcare Analytics
      - ICD-10
      - Revenue Cycle
    properties:
      - type: Documentation
        url: https://www.solventum.com/en-us/home/health-information-systems/
      - type: APIReference
        url: https://developer.solventum.com/
  - aid: solventum:clinical-documentation-improvement
    name: Solventum Clinical Documentation Improvement API
    description: APIs supporting computer-assisted clinical documentation improvement (CDI) workflows, providing real-time query generation, physician query management, and documentation quality analysis to improve specificity, accuracy, and completeness of clinical documentation.
    humanURL: https://www.solventum.com/en-us/home/health-information-systems/clinical-documentation-integrity/
    tags:
      - CDI
      - Clinical Documentation
      - Clinical Documentation Improvement
      - Healthcare IT
      - Physician Query
    properties:
      - type: Documentation
        url: https://www.solventum.com/en-us/home/health-information-systems/clinical-documentation-integrity/
common:
  - type: Website
    url: https://www.solventum.com
  - type: Documentation
    url: https://www.solventum.com/en-us/home/health-information-systems/
  - type: Blog
    url: https://www.solventum.com/en-us/home/about-solventum/newsroom/
  - type: Investors
    url: https://investors.solventum.com/
  - type: LinkedIn
    url: https://www.linkedin.com/company/solventum/
  - type: Support
    url: https://www.solventum.com/en-us/home/contact-us/
  - type: PrivacyPolicy
    url: https://www.solventum.com/en-us/home/privacy/
  - type: TermsOfService
    url: https://www.solventum.com/en-us/home/terms-of-use/
  - type: Features
    data:
      - name: Computer-Assisted Coding
        description: AI-powered ICD-10, CPT, and DRG coding from clinical documentation.
      - name: Clinical Documentation Improvement
        description: Real-time CDI queries and documentation quality analysis.
      - name: DRG Grouping
        description: Diagnosis-related group calculation for inpatient reimbursement.
      - name: Revenue Cycle Management
        description: End-to-end revenue cycle analytics and workflow tools.
      - name: EHR Integration
        description: Native integration with Epic, Cerner, Oracle Health, and other EHR systems.
      - name: Healthcare Analytics
        description: Clinical and financial analytics for quality and performance reporting.
  - type: UseCases
    data:
      - name: Inpatient Coding
        description: Automate ICD-10-CM/PCS coding for inpatient encounters.
      - name: Outpatient Coding
        description: Automate CPT and ICD-10-CM coding for outpatient and ambulatory encounters.
      - name: Quality Reporting
        description: Generate CMS quality measure data for value-based care programs.
      - name: Revenue Optimization
        description: Identify missed revenue opportunities through coding accuracy analysis.
      - name: Clinical Documentation
        description: Improve physician documentation specificity for accurate reimbursement.
  - type: Integrations
    data:
      - name: Epic
        description: Native integration with Epic EHR for embedded coding workflows.
      - name: Oracle Health (Cerner)
        description: Integration with Cerner/Oracle Health for clinical documentation.
      - name: MEDITECH
        description: Integration with MEDITECH EHR platform.
      - name: HL7 FHIR
        description: FHIR-based data exchange for interoperability.
      - name: ICD-10
        description: ICD-10-CM/PCS coding standard support.
      - name: CPT
        description: Current Procedural Terminology coding support.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
