---
aid: charter-communications
name: Charter Communications
description: Charter Communications, Inc. is a leading broadband connectivity company and cable operator serving more than 32 million customers in 41 states through its Spectrum brand. Charter offers internet, TV, mobile, and voice services to residential and business customers, and exposes developer APIs through the Spectrum Enterprise portal for service ticketing and carrier serviceability, and through the Bryte IQ Network-as-a-Service platform built on the Linux Foundation CAMARA project.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/charter-communications/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consumer
tags:
  - Broadband
  - Cable
  - CAMARA
  - Enterprise
  - Network as a Service
  - NaaS
  - Spectrum
  - Telecommunications
  - Ticketing
created: '2026-03-21'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: charter-communications:spectrum-enterprise-api
    name: Charter Communications Spectrum Enterprise API
    description: The Spectrum Enterprise Open API exposes REST endpoints that let enterprise clients integrate their systems with Spectrum Enterprise portal features including service ticket management and carrier serviceability lookups. The API uses OAuth 2.0 authentication.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://enterprise.spectrum.com/
    baseURL: https://enterprise.spectrum.com/api
    tags:
      - Enterprise
      - Networking
      - Telecommunications
      - Ticketing
    properties:
      - type: Documentation
        url: https://enterprise.spectrum.com/
      - type: OpenAPI
        url: openapi/charter-communications-spectrum-enterprise-api-openapi.yml
      - type: Spectral
        url: spectral/charter-communications-spectral.yml
  - aid: charter-communications:bryte-iq-api
    name: Charter Communications Bryte IQ API
    description: Bryte IQ is a Network-as-a-Service (NaaS) API platform from Charter Communications and CableLabs that provides developers with secure, privacy-friendly access to connected device and network capabilities. It is built on the Linux Foundation CAMARA project.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://corporate.charter.com/newsroom/charter-and-cablelabs-launch-bryte-iq-network-as-a-service-platform
    baseURL: https://api.charter.com
    tags:
      - CAMARA
      - NaaS
      - Network as a Service
      - Telecommunications
    properties:
      - type: Documentation
        url: https://corporate.charter.com/newsroom/charter-and-cablelabs-launch-bryte-iq-network-as-a-service-platform
      - type: OpenAPI
        url: openapi/charter-communications-bryte-iq-api-openapi.yml
      - type: CAMARA
        url: https://camaraproject.org/
common:
  - type: Website
    url: https://corporate.charter.com/
  - type: ConsumerSite
    url: https://www.spectrum.com/
  - type: EnterpriseSite
    url: https://enterprise.spectrum.com/
  - type: Newsroom
    url: https://corporate.charter.com/newsroom
  - type: InvestorRelations
    url: https://ir.charter.com/
  - type: Careers
    url: https://jobs.spectrum.com/
  - type: Support
    url: https://www.spectrum.net/support/
  - type: TermsOfService
    url: https://www.spectrum.com/policies/terms-of-service
  - type: PrivacyPolicy
    url: https://www.spectrum.com/policies/your-privacy-rights
  - type: JSONLD
    url: json-ld/charter-communications-context.jsonld
  - type: JSONSchema
    url: json-schema/charter-communications-ticket-schema.json
  - type: JSONSchema
    url: json-schema/charter-communications-serviceability-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
