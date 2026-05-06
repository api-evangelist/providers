---
aid: varian-medical-systems
url: https://raw.githubusercontent.com/api-evangelist/varian-medical-systems/refs/heads/main/apis.yml
name: Varian Medical Systems
tags:
  - Healthcare
  - Oncology
  - Medical Devices
  - FHIR
  - Radiation Therapy
  - Health IT
type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-05-03'
modified: '2026-05-03'
description: Varian Medical Systems is a leading manufacturer of medical devices and software for treating cancer with radiotherapy, radiosurgery, proton therapy, and brachytherapy. Acquired by Siemens Healthineers in 2021, Varian provides the ARIA Oncology Information System (OIS) and developer APIs enabling integration with clinical workflows, EHR systems, and the broader healthcare ecosystem using HL7, DICOM, and FHIR standards.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
apis:
  - aid: varian-medical-systems:aria-fhir-api
    name: ARIA FHIR API
    tags:
      - Healthcare
      - Oncology
      - FHIR
      - Health IT
      - Interoperability
    humanURL: https://varian.dynamicfhir.com/varian/basepractice/r4/Home/ApiDocumentation
    baseURL: https://varian.dynamicfhir.com/fhir/varian/basepractice/r4
    properties:
      - url: https://varian.dynamicfhir.com/varian/basepractice/r4/Home/ApiDocumentation
        type: Documentation
      - url: https://varian.dynamicfhir.com/fhir/varian/basepractice/r4/metadata
        type: CapabilityStatement
      - url: https://raw.githubusercontent.com/api-evangelist/varian-medical-systems/refs/heads/main/openapi/varian-aria-fhir-openapi.yml
        type: OpenAPI
    description: The Varian ARIA FHIR R4 API provides SMART on FHIR access to oncology clinical data from the ARIA Oncology Information System. Supports read and search operations for Patient, Condition, Procedure, Observation, DiagnosticReport, CarePlan, MedicationRequest, and other clinical resources relevant to cancer care.
  - aid: varian-medical-systems:aria-access-api
    name: ARIA Access API
    tags:
      - Healthcare
      - Oncology
      - SOAP
      - Web Services
      - Health IT
    humanURL: https://www.gatewayscripts.com/post/webinars-revisited-a-review-of-aria-apis
    baseURL: https://localhost:55051/Gateway/Service.svc
    properties:
      - url: https://www.gatewayscripts.com/post/webinars-revisited-a-review-of-aria-apis
        type: Documentation
    description: The legacy ARIA Access API provides SOAP and REST access to core ARIA entities including patients, appointments, prescriptions, treatment plans, orders, and administrative data. Deployed on-premise within the healthcare institution's infrastructure.
common:
  - name: ARIA FHIR Developer Portal
    url: https://varian.dynamicfhir.com/varian/basepractice/r4
    type: Portal
  - name: ARIA FHIR API Documentation
    url: https://varian.dynamicfhir.com/varian/basepractice/r4/Home/ApiDocumentation
    type: Documentation
  - name: FHIR Capability Statement
    url: https://varian.dynamicfhir.com/fhir/varian/basepractice/r4/metadata
    type: CapabilityStatement
  - name: ARIA API Overview
    url: https://www.gatewayscripts.com/post/webinars-revisited-a-review-of-aria-apis
    type: Documentation
  - name: ARIA Oncology Information System
    url: https://cancercare.siemens-healthineers.com/products/software/digital-oncology/oncology-management-systems/aria-oncology-information-system
    type: Product
  - name: Varian Website
    url: https://www.varian.com
    type: Website
  - name: Siemens Healthineers Cancer Care
    url: https://cancercare.siemens-healthineers.com
    type: Website
  - name: HL7 FHIR Standard
    url: https://hl7.org/fhir/R4/
    type: Standard
  - name: DICOM Standard
    url: https://www.dicomstandard.org
    type: Standard
---
