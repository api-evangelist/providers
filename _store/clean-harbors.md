---
aid: clean-harbors
name: Clean Harbors
url: https://raw.githubusercontent.com/api-evangelist/clean-harbors/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Emergency Response
  - Environmental Services
  - Hazardous Waste
  - Industrial Services
  - Manifest Tracking
  - Recycling
  - Remediation
description: Clean Harbors is the largest provider of environmental and industrial services in North America, delivering hazardous and non-hazardous waste management, emergency response, industrial cleaning, environmental remediation, and used-oil and solvent recycling through its Safety-Kleen subsidiary. Clean Harbors does not publish a public developer portal or general-purpose REST API surface; programmatic interfaces are limited to the authenticated customer portal at clhsaas.cleanharbors.com (CLH SaaS) for service requests, manifests, and reporting, and partner-mediated EDI feeds. Customers also use the EPA e-Manifest system for federally regulated hazardous-waste manifest tracking.
apis: []
artifacts:
  - aid: clean-harbors:customer-portal
    name: Clean Harbors Customer Portal (CLH SaaS)
    tags:
      - Customer Portal
      - Manifests
      - Service Requests
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://clhsaas.cleanharbors.com/
    properties:
      - url: https://clhsaas.cleanharbors.com/
        type: Portal
    description: Authenticated web portal for Clean Harbors customers to submit service requests, view manifests and shipments, retrieve invoices and reports, and manage account profile information.
  - aid: clean-harbors:e-manifest
    name: EPA e-Manifest Integration
    tags:
      - EPA
      - e-Manifest
      - RCRA
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.epa.gov/e-manifest
    properties:
      - url: https://www.epa.gov/e-manifest
        type: Documentation
    description: Clean Harbors interoperates with the federal EPA e-Manifest system for electronic creation, signing, and tracking of hazardous-waste manifests under RCRA, which exposes its own public APIs at manifest.epa.gov.
common:
  - type: Website
    url: https://www.cleanharbors.com/
  - type: Customer Portal
    url: https://clhsaas.cleanharbors.com/
  - type: Safety-Kleen
    url: https://www.safety-kleen.com/
  - type: Investor Relations
    url: https://investors.cleanharbors.com/
  - type: Privacy Policy
    url: https://www.cleanharbors.com/privacy-policy
  - type: Terms of Service
    url: https://www.cleanharbors.com/terms-of-use
  - type: Support
    url: https://www.cleanharbors.com/contact-us
  - type: Status
    url: https://www.cleanharbors.com/contact-us
  - type: JSON-LD
    url: json-ld/clean-harbors-context.jsonld
  - type: Naftiko Capabilities
    url: capabilities/clean-harbors-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
