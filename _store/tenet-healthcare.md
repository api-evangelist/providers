---
name: Tenet Healthcare
description: Tenet Healthcare is a diversified healthcare services company and Fortune 500 organization operating regionally focused, integrated healthcare delivery networks. The company operates acute care hospitals, ambulatory surgery centers (ASCs), and physician practices across the United States through United Surgical Partners International (USPI) and Tenet Health. Tenet also provides revenue cycle management services through Conifer Health Solutions.
url: https://raw.githubusercontent.com/api-evangelist/tenet-healthcare/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Healthcare
  - Hospitals
  - Ambulatory Surgery Centers
  - Revenue Cycle Management
  - Fortune 500
apis:
  - name: Conifer Health Solutions Revenue Cycle API
    description: Revenue cycle management API from Conifer Health Solutions, a Tenet Healthcare subsidiary providing end-to-end RCM services including patient access, health information management, patient financial services, and clinical revenue integrity for hospitals and health systems.
    humanURL: https://www.coniferhealth.com/
    baseURL: https://api.coniferhealth.com
    tags:
      - Revenue Cycle Management
      - Healthcare Finance
      - Patient Access
      - Claims Management
      - Healthcare
    properties:
      - type: Website
        url: https://www.coniferhealth.com/
      - type: Documentation
        url: https://www.coniferhealth.com/services/
  - name: USPI Ambulatory Surgery Center API
    description: United Surgical Partners International (USPI) integration APIs for ambulatory surgery center scheduling, patient registration, procedure management, and clinical data exchange. USPI operates over 600 ambulatory surgery centers and surgical hospitals across the United States.
    humanURL: https://www.uspi.com/
    baseURL: https://api.uspi.com
    tags:
      - Ambulatory Surgery Centers
      - Surgical Scheduling
      - Patient Registration
      - Healthcare
    properties:
      - type: Website
        url: https://www.uspi.com/
      - type: Documentation
        url: https://www.uspi.com/for-physicians/
  - name: Tenet Health Patient Portal API
    description: Patient-facing digital health API enabling access to medical records, appointment scheduling, test results, care team communications, and bill payment across Tenet Health hospital network. Integrates with MyChart and other patient portal platforms. HL7 FHIR R4 compatible.
    humanURL: https://www.tenethealth.com/patients
    baseURL: https://api.tenethealth.com/patient
    tags:
      - Patient Portal
      - Medical Records
      - Appointment Scheduling
      - FHIR
      - Healthcare
    properties:
      - type: Website
        url: https://www.tenethealth.com/patients
      - type: FHIR Standard
        url: https://hl7.org/fhir/R4/
      - type: OpenAPI
        url: openapi/tenet-healthcare-fhir-openapi.yml
common:
  - type: Website
    url: https://www.tenethealth.com
  - type: Corporate Website
    url: https://www.tenetcorporate.com
  - type: Investor Relations
    url: https://ir.tenethealth.com
  - type: Press Room
    url: https://www.tenethealth.com/news
  - type: Careers
    url: https://careers.tenethealth.com
  - type: Conifer Health Solutions
    url: https://www.coniferhealth.com
  - type: USPI
    url: https://www.uspi.com
  - type: JSON-LD
    url: json-ld/tenet-healthcare-context.jsonld
  - type: JSONSchema
    url: json-schema/tenet-healthcare-patient-schema.json
  - type: JSONSchema
    url: json-schema/tenet-healthcare-appointment-schema.json
  - type: JSONStructure
    url: json-structure/tenet-healthcare-patient-structure.json
  - type: SpectralRules
    url: rules/tenet-healthcare-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/patient-care.yaml
  - type: Vocabulary
    url: vocabulary/tenet-healthcare-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
