---
aid: amtrust-financial-services
url: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/apis.yml
modified: '2026-04-19'
name: AmTrust Financial Services
description: AmTrust Financial Services is a multinational specialty property and casualty insurer focused on small to mid-sized businesses. AmTrust provides APIs that enable insurance agents, brokers, and technology partners to review appetite, generate quotes, and bind policies programmatically. The API platform processes over 12 million API calls daily with 99.68% availability and supports workers' compensation, business owners' policies, general liability, and other commercial insurance products across 300+ eligible class codes.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Commercial Insurance
  - Insurance
  - Property And Casualty
  - Small Business
  - Workers Compensation
apis:
  - aid: amtrust-financial-services:commercial-lines-api
    name: AmTrust Commercial Lines API
    description: The AmTrust Commercial Lines API enables insurance agents, brokers, and technology partners to programmatically review coverage appetite, generate quotes, and bind commercial lines policies. It supports workers' compensation, business owners' policy, general liability, and commercial package products across 300+ eligible class codes.
    tags:
      - Commercial Lines
      - Commercial Package
      - General Liability
      - Insurance
      - Workers Compensation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.amtrustservices.com
    humanURL: https://amtrustfinancial.com/api
    properties:
      - url: https://amtrustfinancial.com/api
        type: Documentation
      - url: https://utapiportal.amtrustgroup.com
        type: Portal
      - url: https://utapiportal.amtrustgroup.com/authentication
        type: Authentication
      - url: openapi/amtrust-financial-services-commercial-lines-api.yaml
        type: OpenAPI
common:
  - type: Portal
    url: https://amtrustfinancial.com
  - type: DeveloperPortal
    url: https://utapiportal.amtrustgroup.com
  - type: Documentation
    url: https://amtrustfinancial.com/api
  - type: Authentication
    url: https://utapiportal.amtrustgroup.com/authentication
  - type: SignUp
    url: https://amtrustfinancial.com/api
  - type: Support
    url: https://amtrustfinancial.com/contact-us
  - type: TermsOfService
    url: https://amtrustfinancial.com/terms-of-use
  - type: PrivacyPolicy
    url: https://amtrustfinancial.com/privacy-policy
  - type: Features
    data:
      - name: Appetite Check
        description: Review coverage eligibility for specific business classes and risk profiles.
      - name: Instant Quoting
        description: Generate commercial lines quotes in real time via API.
      - name: Online Binding
        description: Bind policies programmatically for eligible class codes.
      - name: 300+ Class Codes
        description: Access over 300 bind-online eligible class codes.
      - name: OAuth 2.0 Authentication
        description: Token-based authentication with 4-hour access tokens.
      - name: High Availability
        description: 12 million daily API calls with 99.68% uptime SLA.
  - type: UseCases
    data:
      - name: Agent Platform Integration
        description: Embed AmTrust quoting and binding in agent management systems.
      - name: Wholesale Brokerage Automation
        description: Automate workers' compensation submissions from wholesale platforms.
      - name: AMS Software Integration
        description: Connect agency management software to AmTrust for policy lifecycle management.
      - name: Workers Compensation Automation
        description: Streamline small business workers' compensation from quote to bind.
  - type: Integrations
    data:
      - name: Appulate
        description: Workers' compensation digital submission integration.
      - name: Semsee
        description: Commercial lines quoting platform integration.
      - name: Tarmika
        description: Commercial lines quoting marketplace integration.
      - name: IBQ Systems
        description: Commercial lines rating platform integration.
  - type: SpectralRules
    url: rules/amtrust-financial-services-spectral-rules.yml
  - type: JSONSchema
    url: json-schema/amtrust-financial-services-quote-request-schema.json
  - type: JSONSchema
    url: json-schema/amtrust-financial-services-quote-response-schema.json
  - type: JSONSchema
    url: json-schema/amtrust-financial-services-policy-schema.json
  - type: JSONLD
    url: json-ld/amtrust-financial-services-context.jsonld
  - type: Vocabulary
    url: vocabulary/amtrust-financial-services-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amtrust-insurance-quoting-and-binding.yaml
  - type: JSONStructure
    url: json-structure/amtrust-financial-services-quote-request-structure.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
