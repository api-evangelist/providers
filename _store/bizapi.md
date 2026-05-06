---
aid: bizapi
url: https://raw.githubusercontent.com/api-evangelist/bizapi/refs/heads/main/apis.yml
name: BizAPI
description: BizAPI is a real-time Business Intelligence API from the NAICS Association that provides firmographic data on over 220 million US and international business entities. It enables businesses to enrich CRM records, power customer acquisition workflows, and append NAICS codes, SIC codes, DUNS numbers, company details, sales volume, employee counts, and corporate hierarchy information to any business record via a simple REST API.
tags:
  - Business Intelligence
  - Company Data
  - CRM
  - Firmographic Data
  - NAICS
  - SIC
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-24'
modified: '2026-04-19'
position: Consuming
specificationVersion: '0.19'
apis:
  - aid: bizapi:bizapi
    name: BizAPI Business Intelligence API
    description: Real-time REST API from the NAICS Association that returns firmographic data on over 220 million US and international business locations. Provides DUNS numbers, SIC codes, NAICS codes, company details, contact information, sales volume, employee counts, and corporate hierarchy. Supports both live production and test (sandbox) endpoints. Rate limited to 3 requests per rolling second. Authentication via HTTP Basic with credentials provided at account activation.
    humanURL: https://www.naics.com/business-intelligence-api/
    tags:
      - Business Intelligence
      - Company Data
      - Firmographic Data
      - NAICS
      - SIC
    properties:
      - type: Documentation
        url: https://www.naics.com/business-intelligence-api/
      - type: OpenAPI
        url: openapi/bizapi-business-intelligence-api-openapi.yml
      - type: JSONSchema
        url: json-schema/bizapi-company-schema.json
      - type: JSONStructure
        url: json-structure/bizapi-company-structure.json
      - type: JSONLD
        url: json-ld/bizapi-context.jsonld
      - type: Example
        url: examples/bizapi-company-example.json
common:
  - type: Website
    url: https://www.naics.com/
  - type: Documentation
    url: https://www.naics.com/business-intelligence-api/
  - type: SignUp
    url: https://www.naics.com/bizapi-details/
  - type: Authentication
    url: https://www.naics.com/business-intelligence-api/
  - type: SpectralRules
    url: rules/bizapi-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/bizapi-business-intelligence.yaml
  - type: Vocabulary
    url: vocabulary/bizapi-vocabulary.yaml
  - type: Features
    data:
      - name: Real-Time Firmographic Data
        description: Returns live firmographic data on over 220 million US and international business entities in real time.
      - name: NAICS and SIC Classification
        description: Provides 6-digit NAICS codes and 4- and 8-digit SIC codes for industry classification of business entities.
      - name: DUNS Number Lookup
        description: Returns D&B DUNS numbers enabling universal business entity identification and credit data linkage.
      - name: Corporate Hierarchy
        description: Exposes parent, domestic ultimate, and global ultimate company relationships with DUNS and name fields.
      - name: CRM Enrichment
        description: Designed to integrate with CRMs, SFAs, and internal systems to append firmographic data to business records.
      - name: Sandbox Test Endpoint
        description: Includes a /cosearchtest endpoint that returns fake data without consuming API credits for development and testing.
  - type: UseCases
    data:
      - name: CRM Data Enrichment
        description: Append NAICS codes, DUNS numbers, employee counts, and sales volume to company records in CRM and SFA systems.
      - name: Customer Acquisition
        description: Identify and qualify business prospects by searching firmographic data to match against target industry and size criteria.
      - name: Market Research
        description: Analyze business landscapes by querying firmographic data across industries, geographies, and corporate hierarchies.
      - name: Lead Scoring
        description: Enrich inbound leads with firmographic attributes to power scoring models that prioritize high-value accounts.
      - name: Compliance Verification
        description: Verify business identity, location, and corporate hierarchy for compliance and due diligence workflows.
  - type: Integrations
    data:
      - name: Salesforce
        description: Integrate BizAPI with Salesforce CRM to auto-append firmographic data to account and lead records.
      - name: HubSpot
        description: Enrich HubSpot company records with NAICS, SIC, DUNS, and financial indicators via BizAPI.
      - name: Marketo
        description: Append industry classification and company size data to Marketo lead records for segmentation and scoring.
      - name: Microsoft Dynamics
        description: Connect BizAPI to Dynamics 365 to surface firmographic context on accounts and contacts.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
