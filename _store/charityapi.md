---
aid: charityapi
name: CharityAPI
description: CharityAPI provides a simple REST API for data about US nonprofits and charities sourced directly from IRS filings. Developers can retrieve nonprofit records by EIN, verify whether an organization is a public charity (501c3) with tax-deductible status, and integrate organization name autocomplete to power donation, vetting, and compliance workflows.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/charityapi/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consumer
tags:
  - 501c3
  - Charities
  - Donations
  - EIN
  - IRS
  - Non-Profits
  - Tax Compliance
  - Verification
created: '2025-03-01'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: charityapi:charityapi
    name: CharityAPI
    description: CharityAPI provides REST endpoints for looking up US nonprofit organizations by EIN, performing public charity 501c3 verification checks, and powering autocomplete search across the IRS Business Master File. The API supports donation platforms, fundraising tools, and compliance workflows that need authoritative tax-status data.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://charityapi.org/
    baseURL: https://api.charityapi.org/api
    tags:
      - 501c3
      - Charities
      - EIN
      - IRS
      - Non-Profits
      - Verification
    properties:
      - type: Documentation
        url: https://docs.charityapi.org/
      - type: GettingStarted
        url: https://docs.charityapi.org/main
      - type: Authentication
        url: https://docs.charityapi.org/authentication
      - type: Organizations
        url: https://docs.charityapi.org/organizations
      - type: Pricing
        url: https://www.charityapi.org/pricing
      - type: SignUp
        url: https://www.charityapi.org/get-started
      - type: OpenAPI
        url: openapi/charityapi-openapi.yml
      - type: Spectral
        url: spectral/charityapi-spectral.yml
      - type: NaftikoCapabilities
        url: naftiko/charityapi-capabilities.yml
common:
  - type: Website
    url: https://www.charityapi.org/
  - type: Documentation
    url: https://docs.charityapi.org/
  - type: Pricing
    url: https://www.charityapi.org/pricing
  - type: Blog
    url: https://www.charityapi.org/blog
  - type: SignUp
    url: https://www.charityapi.org/get-started
  - type: Support
    url: https://www.charityapi.org/contact
  - type: TermsOfService
    url: https://www.charityapi.org/terms
  - type: PrivacyPolicy
    url: https://www.charityapi.org/privacy
  - type: JSONLD
    url: json-ld/charityapi-context.jsonld
  - type: JSONSchema
    url: json-schema/charityapi-organization-schema.json
  - type: JSONSchema
    url: json-schema/charityapi-public-charity-check-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
