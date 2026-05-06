---
aid: cvs-health
name: CVS Health
x-type: company
description: CVS Health is a Fortune 50 healthcare services and retail pharmacy company. Its core operating units include CVS Pharmacy (retail pharmacy and mail-order), CVS Caremark (pharmacy benefit management / PBM), Aetna (health insurance, Medicare, Medicaid, dental and vision), MinuteClinic (walk-in clinics), Oak Street Health (primary care for Medicare patients), and Signify Health (in-home health evaluations). CVS Health does not currently operate a public developer portal or generally available REST API. Programmatic integrations with CVS Pharmacy, Caremark, and Aetna are typically established through business partnership agreements, EDI / NCPDP pharmacy networks, and HIPAA-aligned interoperability channels (e.g., FHIR endpoints exposed to qualifying healthcare partners under regulatory mandates such as the CMS Interoperability Rule). Developer-facing artifacts in this index are limited to public marketing, corporate, and digital health references.
url: https://raw.githubusercontent.com/api-evangelist/cvs-health/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consuming
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Aetna
  - Caremark
  - CVS Pharmacy
  - Digital Health
  - FHIR
  - Health Insurance
  - Healthcare
  - HIPAA
  - Interoperability
  - Medicare
  - MinuteClinic
  - Oak Street Health
  - Pharmacy
  - Pharmacy Benefits Management
  - Prescriptions
  - Retail Pharmacy
  - Signify Health
apis:
  - aid: cvs-health:partner-integrations
    name: CVS Health Partner Integrations
    description: CVS Health does not publish a unified public REST API or developer portal. Pharmacy, PBM, and Aetna integrations are conducted via contracted partner channels using industry-standard rails such as NCPDP SCRIPT for e-prescribing, NCPDP Telecom for claims, X12 EDI for healthcare transactions, and HL7 / FHIR endpoints required for CMS Interoperability and Patient Access compliance. This entry catalogs the public corporate, digital health, and regulatory references useful for partner onboarding research.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cvshealth.com/social-responsibility/digital-health
    tags:
      - EDI
      - FHIR
      - Healthcare
      - HL7
      - NCPDP
      - Partner Integration
      - Pharmacy
    properties:
      - type: DigitalHealth
        url: https://www.cvshealth.com/social-responsibility/digital-health
      - type: Caremark
        url: https://www.caremark.com/
      - type: Aetna
        url: https://www.aetna.com/
      - type: MinuteClinic
        url: https://www.cvs.com/minuteclinic/
common:
  - type: Website
    url: https://www.cvshealth.com/
  - type: AboutUs
    url: https://www.cvshealth.com/about
  - type: BusinessStrategy
    url: https://www.cvshealth.com/about/business-strategy.html
  - type: DigitalHealth
    url: https://www.cvshealth.com/social-responsibility/digital-health
  - type: CVSPharmacy
    url: https://www.cvs.com/
  - type: Caremark
    url: https://www.caremark.com/
  - type: Aetna
    url: https://www.aetna.com/
  - type: MinuteClinic
    url: https://www.cvs.com/minuteclinic/
  - type: OakStreetHealth
    url: https://www.oakstreethealth.com/
  - type: SignifyHealth
    url: https://www.signifyhealth.com/
  - type: Newsroom
    url: https://www.cvshealth.com/news
  - type: Careers
    url: https://jobs.cvshealth.com/
  - type: PrivacyPolicy
    url: https://www.cvshealth.com/legal/privacy-policy.html
  - type: TermsOfUse
    url: https://www.cvshealth.com/legal/terms-of-use.html
  - type: LinkedIn
    url: https://www.linkedin.com/company/cvs-health/
  - type: Twitter
    url: https://twitter.com/CVSHealth
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
