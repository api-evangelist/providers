---
aid: department-of-homeland-security
name: Department of Homeland Security
description: The U.S. Department of Homeland Security (DHS) is a cabinet-level federal agency responsible for protecting the nation from terrorism, securing borders, enforcing immigration law, responding to disasters, and securing cyberspace. DHS exposes APIs across its operational components, including FEMA's OpenFEMA platform, USCIS's Developer Portal, the CISA Known Exploited Vulnerabilities catalog, the National Terrorism Advisory System (NTAS) feed, and the DHS Open Data Catalog.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CISA
  - Cybersecurity
  - Disaster
  - Federal Government
  - FEMA
  - Homeland Security
  - Immigration
  - NTAS
  - Open Data
  - USCIS
url: https://raw.githubusercontent.com/api-evangelist/department-of-homeland-security/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: government
position: Producer
access: Public
apis:
  - aid: department-of-homeland-security:openfema-api
    name: OpenFEMA API
    description: The OpenFEMA API is FEMA's public RESTful service that exposes more than 70 datasets including disaster declarations, public assistance funded projects, individual assistance grants, hazard mitigation, and housing assistance program data. The API is free, requires no API key, and supports OData-style query string parameters for filtering, sorting, pagination, and field selection. Default page size is 1,000 records up to a maximum of 10,000.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.fema.gov/about/openfema
    baseURL: https://www.fema.gov/api/open
    tags:
      - Disaster
      - FEMA
      - Hazard Mitigation
      - Public Assistance
    properties:
      - type: Documentation
        url: https://www.fema.gov/about/openfema/api
      - type: Developer Resources
        url: https://www.fema.gov/about/openfema/developer-resources
      - type: Datasets
        url: https://www.fema.gov/about/openfema/data-sets
      - type: Changelog
        url: https://www.fema.gov/about/openfema/changelog
    contact:
      - FN: OpenFEMA
        email: openfema@fema.dhs.gov
        url: https://www.fema.gov/about/openfema
  - aid: department-of-homeland-security:uscis-case-status-api
    name: USCIS Case Status API
    description: The USCIS Case Status API provides programmatic access to the same Case Status Online lookup that immigration applicants use, allowing authorized partners to retrieve the current status and history of a USCIS case by receipt number. The API uses OAuth 2.0 client credentials and is published through the USCIS Developer Portal.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.uscis.gov/api/case-status
    baseURL: https://api.uscis.gov
    tags:
      - Case Status
      - Immigration
      - USCIS
    properties:
      - type: Documentation
        url: https://developer.uscis.gov/api/case-status
      - type: Portal
        url: https://developer.uscis.gov/
      - type: Catalog
        url: https://developer.uscis.gov/apis
    contact:
      - FN: USCIS Developer Support
        url: https://developer.uscis.gov/
  - aid: department-of-homeland-security:uscis-foia-api
    name: USCIS FOIA Request and Status API
    description: The USCIS FOIA Request and Status API allows partners to submit Freedom of Information Act requests programmatically and check the status of submitted requests. It is published through the USCIS Developer Portal using OAuth 2.0.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.uscis.gov/api/foia-request-and-status
    baseURL: https://api.uscis.gov
    tags:
      - FOIA
      - Immigration
      - USCIS
    properties:
      - type: Documentation
        url: https://developer.uscis.gov/api/foia-request-and-status
      - type: Portal
        url: https://developer.uscis.gov/
    contact:
      - FN: USCIS Developer Support
        url: https://developer.uscis.gov/
  - aid: department-of-homeland-security:cisa-kev-feed
    name: CISA Known Exploited Vulnerabilities Catalog Feed
    description: The CISA Known Exploited Vulnerabilities (KEV) catalog is a curated list of vulnerabilities that have been actively exploited in the wild. The catalog is published as a JSON and CSV feed by the Cybersecurity and Infrastructure Security Agency (CISA), and is mirrored on GitHub for easy programmatic access.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
    baseURL: https://www.cisa.gov/sites/default/files/feeds
    tags:
      - CISA
      - CVE
      - Cybersecurity
      - KEV
      - Vulnerabilities
    properties:
      - type: Documentation
        url: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
      - type: JSON Feed
        url: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
      - type: KEV Resources
        url: https://www.cisa.gov/resources-tools/resources/kev-catalog
      - type: Mirror
        url: https://github.com/cisagov/kev-data
    contact:
      - FN: CISA Central
        url: https://www.cisa.gov/about/contact
  - aid: department-of-homeland-security:ntas-feed
    name: National Terrorism Advisory System Feed
    description: The National Terrorism Advisory System (NTAS) feed publishes current terrorism alerts and bulletins issued by DHS as XML files. Developers can consume the feed to surface advisory content in their own applications and web pages.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.dhs.gov/ntas-api-documentation
    baseURL: https://www.dhs.gov
    tags:
      - Alerts
      - NTAS
      - Terrorism
      - XML
    properties:
      - type: Documentation
        url: https://www.dhs.gov/ntas-api-documentation
      - type: NTAS
        url: https://www.dhs.gov/national-terrorism-advisory-system
    contact:
      - FN: DHS Public Affairs
        url: https://www.dhs.gov/contact-us
  - aid: department-of-homeland-security:dhs-open-data-catalog
    name: DHS Open Data Catalog
    description: The DHS Open Data Catalog publishes datasets across the Department's mission areas (immigration, law enforcement, emergency management, cybersecurity, infrastructure protection, screening, and maritime). Datasets are also available via Data.gov's CKAN-compatible API.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.dhs.gov/data
    baseURL: https://catalog.data.gov/api/3
    tags:
      - CKAN
      - Datasets
      - Open Data
    properties:
      - type: Documentation
        url: https://www.dhs.gov/data
      - type: OHSS
        url: https://ohss.dhs.gov/
      - type: Data.gov DHS
        url: https://catalog.data.gov/organization/dhs-gov
      - type: CKAN Reference
        url: https://docs.ckan.org/en/2.8/api/
    contact:
      - FN: DHS Open Data
        url: https://www.dhs.gov/data
common:
  - type: Website
    url: https://www.dhs.gov
  - type: Open Data
    url: https://www.dhs.gov/data
  - type: Office of Homeland Security Statistics
    url: https://ohss.dhs.gov/
  - type: FEMA
    url: https://www.fema.gov
  - type: USCIS Developer Portal
    url: https://developer.uscis.gov/
  - type: CISA
    url: https://www.cisa.gov
  - type: TSA
    url: https://www.tsa.gov
  - type: CBP
    url: https://www.cbp.gov
  - type: ICE
    url: https://www.ice.gov
  - type: Coast Guard
    url: https://www.uscg.mil
  - type: Secret Service
    url: https://www.secretservice.gov
  - type: Components
    url: https://www.dhs.gov/operational-and-support-components
  - type: Data.gov DHS Catalog
    url: https://catalog.data.gov/organization/dhs-gov
  - type: Privacy
    url: https://www.dhs.gov/privacy-office
  - type: Contact
    url: https://www.dhs.gov/contact-us
  - type: GitHub Organization
    url: https://github.com/cisagov
  - type: JSON-LD
    url: json-ld/department-of-homeland-security-context.jsonld
  - type: Vocabulary
    url: vocabulary/department-of-homeland-security-vocabulary.yml
  - type: Capabilities
    url: capabilities/department-of-homeland-security-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
