---
aid: verisk
name: Verisk
description: Verisk (formerly ISO) is a leading data analytics and technology company serving the insurance, energy, and financial services industries. Verisk provides risk scoring, actuarial data, property analytics, catastrophe modeling, claims benchmarking, and underwriting intelligence through RESTful APIs that power insurance pricing, reserving, and exposure management workflows.
url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Insurance
  - Analytics
  - Risk Management
  - Property Data
  - Catastrophe Modeling
  - Underwriting
  - Claims
apis:
  - aid: verisk:insurance-analytics
    name: Verisk Insurance Analytics API
    description: Verisk Insurance Analytics API provides property risk assessments, ISO fire protection classifications, catastrophe peril scores, insurance risk scoring, and claims benchmarking data for P&C insurance carriers. Delivers loss cost data, risk classification, and underwriting data services for insurance pricing, reserving, and exposure management.
    humanURL: https://gateway.verisk.com/docs/MainPage.ashx
    tags:
      - Insurance
      - Analytics
      - Risk Management
      - Property Data
      - Catastrophe Modeling
      - Underwriting
      - Claims
    properties:
      - type: Documentation
        url: https://gateway.verisk.com/docs/MainPage.ashx
      - type: GettingStarted
        url: https://gateway.verisk.com/docs/Getting-Started.ashx
      - type: Authentication
        url: https://gateway.verisk.com/docs/Authentication.ashx
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/openapi/verisk-insurance-analytics-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-property-risk-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-construction-data-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-fire-protection-class-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-address-lookup-request-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-property-lookup-response-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-risk-score-request-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-risk-score-response-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-peril-score-request-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-peril-score-response-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-claims-benchmarks-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-address-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-schema/insurance-analytics-coordinates-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-structure/insurance-analytics-property-risk-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-structure/insurance-analytics-construction-data-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-structure/insurance-analytics-fire-protection-class-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-structure/insurance-analytics-claims-benchmarks-structure.json
      - type: JSON-LD
        url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/json-ld/verisk-insurance-analytics-context.jsonld
  - aid: verisk:underwriting-api
    name: Verisk UnderWriting API
    description: Verisk UnderWriting API provides personal and commercial lines insurance underwriting data including homeowner data, motor vehicle reports, A-PLUS auto and property reports, LightSpeed prefill, geocoding, ISO fire protection class, and coverage verification for P&C insurance carriers. Supports both JSON and XML response formats.
    humanURL: https://gateway.verisk.com/docs/MainPage.ashx
    tags:
      - Underwriting
      - Insurance
      - Personal Lines
      - Commercial Lines
      - Motor Vehicle
      - Property Data
    properties:
      - type: Documentation
        url: https://gateway.verisk.com/docs/MainPage.ashx
      - type: GettingStarted
        url: https://gateway.verisk.com/docs/Getting-Started.ashx
      - type: Authentication
        url: https://gateway.verisk.com/docs/Authentication.ashx
common:
  - type: Website
    url: https://www.verisk.com
  - type: Portal
    url: https://gateway-documentation.verisk.com/
  - type: APIReference
    url: https://apicatalog.verisk.com/
  - type: Documentation
    url: https://gateway.verisk.com/docs/MainPage.ashx
  - type: GettingStarted
    url: https://gateway.verisk.com/docs/Getting-Started.ashx
  - type: Authentication
    url: https://gateway.verisk.com/docs/Authentication.ashx
  - type: TermsOfService
    url: https://www.verisk.com/terms-of-use/
  - type: PrivacyPolicy
    url: https://www.verisk.com/privacy-policy/
  - type: Contact
    url: https://www.verisk.com/contact/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/rules/verisk-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/vocabulary/verisk-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/capabilities/insurance-underwriting.yaml
  - type: Features
    data:
      - name: Property Risk Assessment
        description: Comprehensive property risk scoring including construction, fire protection class, and hazard exposure for fire, wind, hail, flood, and earthquake perils.
      - name: ISO Fire Protection Classification
        description: ISO Public Protection Classification (PPC) grading measuring community fire suppression capability on a 1-10 scale.
      - name: Catastrophe Peril Scoring
        description: Natural hazard exposure scores for hurricane, tornado, hail, wildfire, earthquake, and flood risk used for catastrophe risk management.
      - name: Insurance Risk Scoring
        description: Risk scores for properties, policies, and portfolios including fire protection class, building code effectiveness grading, flood zone, and earthquake zone scores.
      - name: Claims Benchmarking
        description: Industry claims benchmarking data for loss frequency, severity, combined ratio, and loss ratio metrics across lines of business and states.
      - name: Address Geocoding and Lookup
        description: Address-to-property resolution with geocoding to USGS coordinates and ISO property identification for prefill and underwriting workflows.
      - name: Prefill and Accelerated Underwriting
        description: LightSpeed and homeowner data APIs provide instant underwriting intelligence from a business name and address for small commercial and personal lines.
      - name: Weather Analytics Integration
        description: Benchmark API provides hail, wind, lightning, and hurricane wind analytics for property and auto claims and underwriting decisions.
  - type: UseCases
    data:
      - name: Insurance Pricing and Rating
        description: Use risk scores and property data to accurately price insurance policies for homeowners, auto, and commercial lines of business.
      - name: Catastrophe Risk Management
        description: Assess portfolio exposure to natural hazard perils and estimate probable maximum loss (PML) for catastrophe reinsurance programs.
      - name: Claims Adjudication
        description: Integrate weather analytics and property data to streamline field adjustments, reduce inspection costs, and accelerate claim cycle times.
      - name: Underwriting Automation
        description: Automate underwriting decisions by integrating prefill data, motor vehicle reports, and coverage verification into policy administration systems.
      - name: Portfolio Risk Monitoring
        description: Monitor geographic concentration and peril exposure across insurance portfolios for risk management and regulatory reporting.
  - type: Integrations
    data:
      - name: Policy Administration Systems
        description: Integrate risk scores and underwriting data directly into existing policy administration and underwriting workflow systems.
      - name: Claims Management Systems
        description: Embed weather analytics and property data into claims management platforms for faster adjudication.
      - name: Catastrophe Modeling Platforms
        description: Feed peril scores and property data into catastrophe modeling platforms like AIR Worldwide and RMS for exposure analysis.
      - name: Generative AI Underwriting Assistant
        description: API-enabled GenAI commercial underwriting assistant that integrates into existing policy administration systems.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
