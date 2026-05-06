---
aid: abortion-policy-api
url: https://raw.githubusercontent.com/api-evangelist/abortion-policy-api/refs/heads/main/apis.yml
name: Abortion Policy API
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Abortion
  - Policies
  - Healthcare
  - Government
description: The Abortion Policy API provides up-to-date information on US state abortion policies that can be integrated into online abortion resources. The API consolidates abortion laws into one database across four data tables covering gestational limits, insurance coverage, minors restrictions, and waiting periods. Data is accessible by US state name or zip code. The project is co-led by Patient Forward and is fiscally sponsored by NEO Philanthropy.
created: '2025-01-07'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: abortion-policy-api:abortion-policy-api
    name: Abortion Policy API
    tags:
      - Abortion
      - Policies
      - Healthcare
    humanURL: https://www.abortionpolicyapi.com/
    properties:
      - type: Documentation
        url: https://www.abortionpolicyapi.com/
      - type: Authentication
        url: https://www.abortionpolicyapi.com/request-access
      - type: APIReference
        url: https://www.abortionpolicyapi.com/field-references
      - type: OpenAPI
        url: openapi/abortion-policy-api-openapi.yml
      - type: CodeExamples
        url: https://github.com/alexanian/abortion-policy-api-examples
        title: Python/JavaScript Examples
      - type: JSONSchema
        url: json-schema/gestational-limits-schema.json
        title: Gestational Limits Schema
      - type: JSONSchema
        url: json-schema/insurance-coverage-schema.json
        title: Insurance Coverage Schema
      - type: JSONSchema
        url: json-schema/minors-restrictions-schema.json
        title: Minors Restrictions Schema
      - type: JSONSchema
        url: json-schema/waiting-periods-schema.json
        title: Waiting Periods Schema
    description: The Abortion Policy API consolidates US state abortion laws into one database for third-party developers to use. Data tables include gestational limits, insurance coverage, minors restrictions, and waiting periods. Access requires requesting an API key. Rate limit is 100 calls per 60 seconds.
common:
  - type: GettingStarted
    url: https://www.abortionpolicyapi.com/
  - type: Authentication
    url: https://www.abortionpolicyapi.com/request-access
  - type: APIReference
    url: https://www.abortionpolicyapi.com/field-references
  - type: CaseStudies
    url: https://www.abortionpolicyapi.com/case-studies
  - type: Support
    url: https://www.abortionpolicyapi.com/contact
  - type: TermsOfService
    url: https://www.abortionpolicyapi.com/terms
  - type: PrivacyPolicy
    url: https://www.abortionpolicyapi.com/privacy
  - type: RateLimits
    data:
      - name: API Calls Per Connection
        description: 100 calls per 60 seconds per connection
  - type: Features
    data:
      - name: Gestational Limits Data
        description: State-by-state gestational limit policies including exceptions for life, health, fetal anomaly, and rape/incest.
      - name: Insurance Coverage Data
        description: Comprehensive insurance coverage restrictions covering Medicaid, private insurance, and ACA exchange plans by state.
      - name: Minors Restrictions Data
        description: Parental consent, notification, and judicial bypass requirements for minors seeking abortion by state.
      - name: Waiting Periods Data
        description: State mandatory waiting period hours and counseling visit requirements between counseling and abortion care.
      - name: State and Zip Code Lookup
        description: All policy data accessible by US state name or 5-digit zip code for integration flexibility.
      - name: Expert-Curated Data
        description: Data collaboratively analyzed by reproductive rights experts from Guttmacher, Planned Parenthood, Power to Decide, CRR, and others.
      - name: Free Public Good
        description: API provided free without gatekeeping as a public good resource for reproductive health organizations.
  - type: UseCases
    data:
      - name: Abortion Finder Applications
        description: Integrate state abortion policy data into patient-facing tools that help people find abortion services.
      - name: Healthcare Provider Tools
        description: Embed policy data into clinical tools to help providers advise patients on state-specific access restrictions.
      - name: Journalism and Research
        description: Access structured policy data for data journalism, academic research, and policy analysis.
      - name: Advocacy and Education
        description: Power public education tools and advocacy platforms with accurate, up-to-date abortion policy information.
      - name: Chatbot Integration
        description: Provide abortion policy answers in conversational tools like Charley the Chatbot.
      - name: Legal Aid Resources
        description: Support legal aid organizations with accurate state law data for advising clients on abortion access.
  - type: Integrations
    data:
      - name: Planned Parenthood
        description: Used by Planned Parenthood for patient-facing abortion policy information.
      - name: Abortion Finder
        description: Powers policy data in the Abortion Finder patient resource tool.
      - name: Charley the Chatbot
        description: Integrated into Charley the Chatbot for conversational abortion policy guidance.
      - name: Ineedana.com
        description: Powers policy data for ineedana.com abortion access resource.
      - name: Microsoft Power Platform
        description: Available as an independent publisher connector for Power Apps, Power Automate, Logic Apps, and Copilot Studio.
  - type: SpectralRules
    url: rules/abortion-policy-api-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/abortion-policy-lookup.yaml
  - type: NaftikoCapability
    url: capabilities/shared/abortion-policy-api.yaml
  - type: Vocabulary
    url: vocabulary/abortion-policy-api-vocabulary.yaml
  - type: JSONLD
    url: json-ld/abortion-policy-api-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
