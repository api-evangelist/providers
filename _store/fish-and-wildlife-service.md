---
aid: fish-and-wildlife-service
name: U.S. Fish and Wildlife Service
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/fish-and-wildlife-service/refs/heads/main/apis.yml
specificationVersion: '0.19'
tags:
  - Conservation
  - Endangered Species
  - Federal Government
  - Fisheries
  - Wildlife
description: The U.S. Fish and Wildlife Service (USFWS) is the federal agency responsible for conserving, protecting, and enhancing fish, wildlife, plants, and their habitats for the continuing benefit of the American people. USFWS programs cover migratory birds, endangered species, interjurisdictional fish and marine mammals, and inland sport fisheries. Public-facing data is shared primarily through web tools and downloadable datasets such as the Environmental Conservation Online System (ECOS), Information for Planning and Consultation (IPaC), and the Service Catalog (ServCat) rather than a consolidated public API program.
created: '2024-12-03'
modified: '2026-04-28'
apis:
  - aid: fish-and-wildlife-service:ecos
    name: USFWS Environmental Conservation Online System (ECOS)
    tags:
      - Critical Habitat
      - Endangered Species
      - Environmental Data
      - Wildlife
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://ecos.fws.gov/ecp/
    description: The Environmental Conservation Online System (ECOS) is the USFWS portal for threatened and endangered species data, critical habitat designations, recovery plans, and Section 7 consultations. ECOS exposes structured species profiles and downloadable datasets, but does not currently publish a stable, fully documented public API contract.
    properties:
      - url: https://ecos.fws.gov/ecp/
        type: Portal
      - url: https://ecos.fws.gov/ecp/report
        type: Reports
  - aid: fish-and-wildlife-service:ipac
    name: USFWS Information for Planning and Consultation (IPaC)
    tags:
      - Endangered Species Act
      - Environmental Review
      - Project Planning
      - Section 7 Consultation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://ipac.ecosphere.fws.gov/
    description: Information for Planning and Consultation (IPaC) is a USFWS web-based project planning tool that helps users identify potential impacts on protected species and habitats, generate official species lists for Endangered Species Act Section 7 consultations, and build consultation packages. IPaC is delivered as an interactive web application and does not currently publish a public API contract.
    properties:
      - url: https://ipac.ecosphere.fws.gov/
        type: Portal
      - url: https://ipac.ecosphere.fws.gov/about
        type: Documentation
  - aid: fish-and-wildlife-service:servcat
    name: USFWS Service Catalog (ServCat)
    tags:
      - Document Repository
      - Reference Library
      - Reports
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://ecos.fws.gov/ServCat/
    description: The Service Catalog (ServCat) is the USFWS reference library for reports, datasets, and other documents produced by or for the agency. ServCat is backed by an internal services layer; while the catalog is publicly browseable, a public API contract is not currently published.
    properties:
      - url: https://ecos.fws.gov/ServCat/
        type: Portal
common:
  - type: Website
    url: https://www.fws.gov
  - type: Data
    url: https://www.fws.gov/library/collections/data
  - type: ECOS
    url: https://ecos.fws.gov/ecp/
  - type: IPaC
    url: https://ipac.ecosphere.fws.gov/
  - type: ServCat
    url: https://ecos.fws.gov/ServCat/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
