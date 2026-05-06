---
aid: nhs-england-digital
name: NHS England Digital
description: NHS England (incorporating the former NHS Digital and NHSX) provides national digital, data, and technology services for the NHS in England. The organization operates the Spine, the Personal Demographics Service, the Electronic Prescription Service, the Summary Care Record, e-Referral Service, NHS App, NHS.uk, and an extensive API platform of FHIR and REST APIs used by health and care providers, developers, and researchers across England.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Clinical
  - Demographics
  - FHIR
  - Government
  - Health
  - Healthcare
  - NHS
  - Open Data
  - Patient Records
  - Prescriptions
  - UK
url: https://raw.githubusercontent.com/api-evangelist/nhs-england-digital/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nhs-england-digital:api-platform
    name: NHS England API Platform
    description: The NHS England API platform hosts a catalogue of national APIs for health and care, including FHIR and REST APIs covering patient demographics, prescriptions, appointments, records, screening, and clinical terminology. The platform provides developer onboarding, sandbox environments, OAuth 2.0 authentication, and production access through API keys and signed JWT authentication.
    humanURL: https://digital.nhs.uk/developer
    tags:
      - API Platform
      - Developer Portal
      - FHIR
      - Healthcare
    properties:
      - type: Documentation
        url: https://digital.nhs.uk/developer
      - type: APIReference
        url: https://digital.nhs.uk/developer/api-catalogue
      - type: GettingStarted
        url: https://digital.nhs.uk/developer/guides-and-documentation
  - aid: nhs-england-digital:personal-demographics-service
    name: Personal Demographics Service (PDS) FHIR API
    description: The Personal Demographics Service is the national electronic database of NHS patient demographic details such as name, address, date of birth and NHS Number. The PDS FHIR API allows authorised systems to retrieve and update patient demographics for citizens registered with the NHS in England, Wales, and the Isle of Man.
    humanURL: https://digital.nhs.uk/developer/api-catalogue/personal-demographics-service-fhir
    tags:
      - Demographics
      - FHIR
      - Patient Records
    properties:
      - type: Documentation
        url: https://digital.nhs.uk/developer/api-catalogue/personal-demographics-service-fhir
  - aid: nhs-england-digital:electronic-prescription-service
    name: Electronic Prescription Service (EPS) FHIR API
    description: The Electronic Prescription Service enables prescribers to send prescriptions electronically to a dispenser of the patient's choice. The EPS FHIR API allows clinical systems to create, retrieve, release, claim, and cancel electronic prescriptions for patients in England.
    humanURL: https://digital.nhs.uk/developer/api-catalogue/electronic-prescription-service-fhir
    tags:
      - FHIR
      - Pharmacy
      - Prescriptions
    properties:
      - type: Documentation
        url: https://digital.nhs.uk/developer/api-catalogue/electronic-prescription-service-fhir
  - aid: nhs-england-digital:e-referral-service
    name: e-Referral Service (e-RS) FHIR API
    description: The NHS e-Referral Service combines electronic booking with a choice of place, date and time for first hospital or clinic appointments. The e-RS FHIR API enables clinical systems to integrate referral and booking workflows directly into the patient pathway.
    humanURL: https://digital.nhs.uk/developer/api-catalogue/e-referral-service-fhir
    tags:
      - Appointments
      - FHIR
      - Referrals
    properties:
      - type: Documentation
        url: https://digital.nhs.uk/developer/api-catalogue/e-referral-service-fhir
  - aid: nhs-england-digital:summary-care-record
    name: Summary Care Record (SCR) API
    description: The Summary Care Record holds essential patient information from the GP record. The SCR API enables authorised health and care professionals to retrieve a patient's medication, allergies and adverse reactions, and any additional information shared by the patient's GP.
    humanURL: https://digital.nhs.uk/developer/api-catalogue/summary-care-record
    tags:
      - Clinical
      - Patient Records
    properties:
      - type: Documentation
        url: https://digital.nhs.uk/developer/api-catalogue/summary-care-record
  - aid: nhs-england-digital:gp-connect
    name: GP Connect API
    description: GP Connect APIs allow authorised clinical systems to view and book GP services. The APIs provide structured access to GP records including medications, allergies, immunisations, observations, problems, and appointment availability across federated GP systems.
    humanURL: https://digital.nhs.uk/developer/api-catalogue/gp-connect-access-record-structured
    tags:
      - Appointments
      - Clinical
      - FHIR
      - GP
      - Patient Records
    properties:
      - type: Documentation
        url: https://digital.nhs.uk/developer/api-catalogue/gp-connect-access-record-structured
  - aid: nhs-england-digital:nhs-login
    name: NHS Login API
    description: NHS login provides a single, secure way for citizens to access NHS digital services. The NHS login API enables relying parties to authenticate users, verify identity to a known level of assurance, and obtain consented identity claims using OpenID Connect.
    humanURL: https://digital.nhs.uk/services/nhs-login
    tags:
      - Authentication
      - Identity
      - OpenID Connect
    properties:
      - type: Documentation
        url: https://digital.nhs.uk/services/nhs-login
common:
  - type: Website
    url: https://digital.nhs.uk
  - type: Documentation
    url: https://digital.nhs.uk/developer
  - type: APIReference
    url: https://digital.nhs.uk/developer/api-catalogue
  - type: GettingStarted
    url: https://digital.nhs.uk/developer/guides-and-documentation
  - type: Blog
    url: https://digital.nhs.uk/blog
  - type: News
    url: https://digital.nhs.uk/news
  - type: Support
    url: https://digital.nhs.uk/about-nhs-digital/contact-us
  - type: StatusPage
    url: https://status.digital.nhs.uk
  - type: GitHubOrganization
    url: https://github.com/NHSDigital
  - type: TermsOfService
    url: https://digital.nhs.uk/about-nhs-digital/terms-and-conditions
  - type: Privacy
    url: https://digital.nhs.uk/about-nhs-digital/privacy-and-cookies
  - type: X
    url: https://x.com/NHSEngland
  - type: YouTube
    url: https://www.youtube.com/c/NHSDigital
  - type: Features
    data:
      - name: National FHIR APIs
        description: HL7 FHIR-based APIs for patient records, prescriptions, referrals, and clinical data exchange.
      - name: Sandbox Environments
        description: Free, anonymous sandbox endpoints for testing API integrations before production access.
      - name: OAuth 2.0 and Signed JWT
        description: Production authentication via OAuth 2.0 user-restricted access and application-restricted signed JWT.
      - name: Developer Onboarding
        description: Structured onboarding pathway from sandbox to integration test to production via Apigee developer portal.
      - name: NHS Login Identity Provider
        description: Citizen-facing OpenID Connect identity provider for NHS digital services.
      - name: Spine Connectivity
        description: National secure messaging and data backbone underlying the major NHS APIs.
  - type: UseCases
    data:
      - name: Clinical System Integration
        description: Integrate EHR and clinical systems with national patient demographics, prescriptions, and records.
      - name: Citizen-Facing Apps
        description: Build apps that authenticate citizens with NHS login and surface their NHS data.
      - name: Pharmacy Workflow
        description: Receive, release, dispense, and claim electronic prescriptions through the EPS API.
      - name: Referral Management
        description: Integrate appointment booking and referral workflows via the e-Referral Service.
      - name: GP Record Access
        description: View structured GP record data across federated systems via GP Connect.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
