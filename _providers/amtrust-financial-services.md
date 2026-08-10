---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Amtrust Financial Services Agentic Access
  operation_count: 7
  slug: amtrust-financial-services-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 4
apis:
- description: Coverage appetite and eligibility checks
  name: AmTrust Financial Services Appetite API
  slug: amtrust-financial-services-appetite-api
- description: OAuth 2.0 token management
  name: AmTrust Financial Services Authentication API
  slug: amtrust-financial-services-authentication-api
- description: Policy binding and management
  name: AmTrust Financial Services Policies API
  slug: amtrust-financial-services-policies-api
- description: Quote generation and management
  name: AmTrust Financial Services Quotes API
  slug: amtrust-financial-services-quotes-api
artifact_total: 50
collections:
- collection_type: postman
  name: AmTrust Financial Services Commercial Lines Appetite API
  slug: postman-amtrust-financial-services-appetite-api
- collection_type: postman
  name: AmTrust Financial Services Commercial Lines Appetite Authentication API
  slug: postman-amtrust-financial-services-authentication-api
- collection_type: postman
  name: AmTrust Financial Services Commercial Lines Appetite Policies API
  slug: postman-amtrust-financial-services-policies-api
- collection_type: postman
  name: AmTrust Financial Services Commercial Lines Appetite Quotes API
  slug: postman-amtrust-financial-services-quotes-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amtrust-financial-services/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amtrust-financial-services-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amtrust-financial-services-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amtrust-financial-services-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amtrust-financial-services-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amtrust
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amtrust-financial-services-inc
- group: start
  title: ''
  type: Portal
  url: https://amtrustfinancial.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://utapiportal.amtrustgroup.com
- group: docs
  title: ''
  type: Documentation
  url: https://amtrustfinancial.com/api
- group: auth
  title: ''
  type: Authentication
  url: https://utapiportal.amtrustgroup.com/authentication
- group: start
  title: ''
  type: Signup
  url: https://amtrustfinancial.com/api
- group: operate
  title: ''
  type: Support
  url: https://amtrustfinancial.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amtrustfinancial.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amtrustfinancial.com/privacy-policy
- group: design
  title: ''
  type: SpectralRules
  url: rules/amtrust-financial-services-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amtrust-financial-services-quote-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amtrust-financial-services-quote-response-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amtrust-financial-services-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amtrust-financial-services-vocabulary.yaml
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amtrust-financial-services-quote-request-structure.json
- group: company
  title: ''
  type: Blog
  url: https://amtrustfinancial.com/blog
description: AmTrust Financial Services is a multinational specialty property and casualty insurer focused on small to mid-sized businesses. AmTrust provides APIs that enable insurance agents, brokers, and technology partners to review appetite, generate quotes, and bind policies programmatically. The API platform processes over 12 million API calls daily with 99.68% availability and supports workers' compensation, business owners' policies, general liability, and other commercial insurance products across 300+ eligible class codes.
examples:
- key_count: 4
  name: Amtrust Financial Services Appetite Request Example
  slug: amtrust-financial-services-appetite-request-example
- key_count: 7
  name: Amtrust Financial Services Policy Example
  slug: amtrust-financial-services-policy-example
- key_count: 6
  name: Amtrust Financial Services Quote Request Example
  slug: amtrust-financial-services-quote-request-example
- key_count: 9
  name: Amtrust Financial Services Quote Response Example
  slug: amtrust-financial-services-quote-response-example
features:
- description: Review coverage eligibility for specific business classes and risk profiles.
  name: Appetite Check
- description: Generate commercial lines quotes in real time via API.
  name: Instant Quoting
- description: Bind policies programmatically for eligible class codes.
  name: Online Binding
- description: Access over 300 bind-online eligible class codes.
  name: 300+ Class Codes
- description: Token-based authentication with 4-hour access tokens.
  name: OAuth 2.0 Authentication
- description: 12 million daily API calls with 99.68% uptime SLA.
  name: High Availability
finops:
- name: Amtrust Financial Services Finops
  service_category: API
  slug: amtrust-financial-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amtrust-financial-services.png
integrations:
- description: Workers' compensation digital submission integration.
  name: Appulate
- description: Commercial lines quoting platform integration.
  name: Semsee
- description: Commercial lines quoting marketplace integration.
  name: Tarmika
- description: Commercial lines rating platform integration.
  name: IBQ Systems
json_schemas:
- name: AppetiteRequest
  property_count: 4
  slug: amtrust-financial-services-appetite-request
- name: AppetiteResponse
  property_count: 4
  slug: amtrust-financial-services-appetite-response
- name: BindRequest
  property_count: 3
  slug: amtrust-financial-services-bind-request
- name: Insured
  property_count: 7
  slug: amtrust-financial-services-insured
- name: PolicyResponse
  property_count: 8
  slug: amtrust-financial-services-policy-response
- name: QuoteRequest
  property_count: 7
  slug: amtrust-financial-services-quote-request
- name: QuoteResponse
  property_count: 10
  slug: amtrust-financial-services-quote-response
json_structures:
- name: Amtrust Financial Services Appetite Request Structure
  property_count: 4
  slug: amtrust-financial-services-appetite-request-structure
- name: Amtrust Financial Services Appetite Response Structure
  property_count: 4
  slug: amtrust-financial-services-appetite-response-structure
- name: Amtrust Financial Services Bind Request Structure
  property_count: 3
  slug: amtrust-financial-services-bind-request-structure
- name: Amtrust Financial Services Insured Structure
  property_count: 7
  slug: amtrust-financial-services-insured-structure
- name: Amtrust Financial Services Policy Response Structure
  property_count: 8
  slug: amtrust-financial-services-policy-response-structure
- name: Amtrust Financial Services Quote Request Structure
  property_count: 7
  slug: amtrust-financial-services-quote-request-structure
- name: Amtrust Financial Services Quote Response Structure
  property_count: 10
  slug: amtrust-financial-services-quote-response-structure
jsonld:
- class_count: 6
  name: Amtrust Financial Services Context
  property_count: 13
  slug: amtrust-financial-services-context
layout: provider
modified: '2026-04-19'
name: AmTrust Financial Services
nav: Providers
network: true
overview: 'AmTrust Financial Services publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Appetite API, Authentication API, Policies API, and 1 more. Tagged areas include Commercial Insurance, Insurance, Property And Casualty, Small Business, and Workers Compensation.


  The AmTrust Financial Services catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AmTrust Financial Services'' developer surface includes authentication, developer portal, documentation, signup flow, support, engineering blog, and 16 more developer resources.'
plans:
- name: Amtrust Financial Services Plans Pricing
  plan_count: 3
  slug: amtrust-financial-services-plans-pricing
press:
- date: '2026-05-25'
  title: AmTrust Improves Outcomes for Injured Employees with ...
  url: https://claraanalytics.com/news/amtrust-scores-a-win-win-with-small-businesses-ensuring-quality-care-for-injured-employees/
- date: '2026-05-25'
  title: AmTrust partners with TCS to transform E&S clearance ...
  url: https://www.tcs.com/what-we-do/industries/insurance/case-study/amtrust-financial-services-transformation
- date: '2026-05-25'
  title: Hagens Berman Alerts Investors in AmTrust Financial ...
  url: https://www.prnewswire.com/news-releases/afsi-investor-alert-hagens-berman-alerts-investors-in-amtrust-financial-services-to-investigation-into-possible-securities-law-violations-related-to-admitted-material-weaknesses-in-internal-controls-over-financial-reporting-300414199.html
- date: '2026-05-25'
  title: AmTrust Financial Services and Blackstone Credit & ...
  url: https://www.sttinfo.fi/tiedote/71449628/amtrust-financial-services-and-blackstone-credit-and-insurance-enter-into-strategic-transaction-for-amtrusts-global-mga-and-fee-businesses?publisherId=58763726&lang=en
- date: '2026-05-25'
  title: 'AmTrust partners with Blackstone: Insurance news'
  url: https://www.dig-in.com/news/amtrust-partners-with-blackstone-insurance-news
random_paper: 7
rate_limits:
- limit_count: 5
  name: Amtrust Financial Services Rate Limits
  slug: amtrust-financial-services-rate-limits
rules:
- name: AmTrust Financial Services API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amtrust-financial-services-jsonschema-spectral-rules
- name: AmTrust Financial Services API Rules
  rule_count: 17
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 10
  slug: amtrust-financial-services-spectral-rules
score:
  band: developing
  composite: 46.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 25.2
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/screenshots/amtrust-financial-services-2026-06-20T171943.png
security:
- kind: authentication
  name: Amtrust Financial Services Authentication
  slug: amtrust-financial-services-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Amtrust Financial Services Domain Security
  slug: amtrust-financial-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amtrust Financial Services Vulnerability Disclosure
  slug: amtrust-financial-services-vulnerability-disclosure
  summary_line: disclosure policy published
slug: amtrust-financial-services
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
- Fortune 1000
use_cases:
- description: Embed AmTrust quoting and binding in agent management systems.
  name: Agent Platform Integration
- description: Automate workers' compensation submissions from wholesale platforms.
  name: Wholesale Brokerage Automation
- description: Connect agency management software to AmTrust for policy lifecycle management.
  name: AMS Software Integration
- description: Streamline small business workers' compensation from quote to bind.
  name: Workers Compensation Automation
website: https://utapiportal.amtrustgroup.com
---
