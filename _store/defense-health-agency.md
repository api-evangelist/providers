---
aid: defense-health-agency
name: Defense Health Agency
url: https://raw.githubusercontent.com/api-evangelist/defense-health-agency/refs/heads/main/apis.yml
description: The Defense Health Agency (DHA) is a joint, integrated combat support agency that enables the Army, Navy, and Air Force medical services to provide a medically ready force and ready medical force to combatant commands. DHA operates the Military Health System (MHS), MHS Genesis electronic health record, the Military Health System Data Repository (MDR), and the Enterprise Intelligence and Data Solutions (EIDS) program. Data exchange inside MHS Genesis uses SMART on FHIR APIs, but DHA does not currently publish a general-purpose public developer API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consuming
specificationVersion: '0.19'
xType: government
tags:
  - Federal Government
  - Defense
  - Department of Defense
  - Health
  - Military Health System
  - MHS Genesis
  - FHIR
  - Health IT
created: '2024-12-03'
modified: '2026-04-28'
apis:
  - aid: defense-health-agency:mhs-genesis-smart-on-fhir
    name: MHS Genesis SMART on FHIR API
    description: MHS Genesis, the Department of Defense electronic health record built on Oracle Health (Cerner), exposes a SMART on FHIR interface for authorized clinical applications to read and write patient data. Access is restricted to vetted application partners and DoD beneficiaries.
    humanURL: https://health.mil/About-MHS/OASDHA/Defense-Health-Agency/Solution-Delivery-Division/MHS-GENESIS
    tags:
      - FHIR
      - SMART on FHIR
      - Electronic Health Record
      - MHS Genesis
    properties:
      - type: Documentation
        url: https://health.mil/About-MHS/OASDHA/Defense-Health-Agency/Solution-Delivery-Division/MHS-GENESIS
common:
  - type: Website
    url: https://www.health.mil
  - type: About DHA
    url: https://www.health.mil/About-MHS/OASDHA/Defense-Health-Agency
  - type: Publications
    url: https://health.mil/Reference-Center/DHA-Publications
  - type: News
    url: https://www.health.mil/News
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
