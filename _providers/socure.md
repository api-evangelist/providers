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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Socure Agentic Access
  operation_count: 12
  slug: socure-agentic-access
  summary_line: 12 operations · 9 acting
api_count: 3
apis:
- description: RiskOS is Socure's identity and fraud orchestration platform that combines ID+ modules, customer-configured workflows, case management, and a no-code rules editor under a unified API. RiskOS Enterpris
  name: Socure RiskOS API
  slug: socure-riskos-api
- description: The Alerts API from socure — 2 operation(s) for alerts.
  name: socure Alerts API
  slug: socure-alerts-api
- description: Unified multi-module identity, fraud, and risk evaluation
  name: socure ID+ API
  slug: socure-id-api
- description: The Monitoring API from socure — 2 operation(s) for monitoring.
  name: socure Monitoring API
  slug: socure-monitoring-api
- description: DocV session orchestration
  name: socure Transactions API
  slug: socure-transactions-api
- description: Document and selfie upload management
  name: socure Uploads API
  slug: socure-uploads-api
arazzos:
- description: Validate a funding bank account, then run a decision evaluation on the account owner when the account is open.
  name: Socure Bank Account Onboarding
  slug: socure-bank-account-onboarding-workflow
- description: Score email, phone, and address risk for an applicant, then run a decision when all contact signals are low risk.
  name: Socure Contact Risk Then Decision
  slug: socure-contact-risk-then-decision-workflow
- description: Verify a government ID through DocV, then fold the document result into an ID+ identity evaluation.
  name: Socure DocV Then Identity
  slug: socure-docv-then-identity-workflow
- description: Create a document verification transaction, upload the ID and selfie, finalize verification, and poll for the outcome.
  name: Socure DocV Verify And Poll
  slug: socure-docv-verify-and-poll-workflow
- description: Screen an applicant for identity fraud, synthetic fraud, and device risk, then enroll watchlist monitoring on a clean result.
  name: Socure Fraud And Device Risk Screen
  slug: socure-fraud-device-risk-screen-workflow
- description: Run a multi-module ID+ evaluation and branch onboarding on the returned decision outcome.
  name: Socure Identity Decision Branch
  slug: socure-identity-decision-branch-workflow
- description: Screen an identity against KYC and global watchlist, then enroll it for ongoing monitoring and confirm the profile.
  name: Socure KYC Watchlist Enroll
  slug: socure-kyc-watchlist-enroll-workflow
- description: Confirm a watchlist monitoring profile is active, then remove it when a customer is offboarded.
  name: Socure Monitoring Offboard
  slug: socure-monitoring-offboard-workflow
- description: List open watchlist monitoring alerts for a profile and move a selected alert through its disposition.
  name: Socure Watchlist Alert Triage
  slug: socure-watchlist-alert-triage-workflow
artifact_total: 69
asyncapis:
- description: Webhook event stream emitted by the Socure Predictive DocV service to notify the integrator of session lifecycle events. The customer registers a webhook URL when creating a DocV transaction; Socure P
  name: Socure DocV Webhooks
  slug: socure-docv-asyncapi
- description: Webhook event stream emitted by the Socure Global Watchlist Monitoring service. Once a profile is enrolled for continuous monitoring, Socure POSTs alert events to the integrator's registered webhook U
  name: Socure Global Watchlist Monitoring Webhooks
  slug: socure-watchlist-asyncapi
collections:
- collection_type: postman
  name: Socure Account Intelligence API
  slug: postman-socure-account-intelligence-api
- collection_type: postman
  name: Socure Decision API
  slug: postman-socure-decision-api
- collection_type: postman
  name: Socure Predictive DocV API
  slug: postman-socure-docv-api
- collection_type: postman
  name: Socure ID+ API
  slug: postman-socure-idplus-api
- collection_type: postman
  name: Socure Global Watchlist Monitoring API
  slug: postman-socure-watchlist-monitoring-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Socure Account Intelligence API
  slug: open-socure-account-intelligence-api
- collection_type: open
  name: Socure Account Intelligence Alerts API
  slug: open-socure-alerts-api
- collection_type: open
  name: Socure Account Intelligence Decision API
  slug: open-socure-decision-api
- collection_type: open
  name: Socure Predictive DocV API
  slug: open-socure-docv-api
- collection_type: open
  name: Socure Account Intelligence ID+ API
  slug: open-socure-id-api
- collection_type: open
  name: Socure ID+ API
  slug: open-socure-idplus-api
- collection_type: open
  name: Socure Account Intelligence Monitoring API
  slug: open-socure-monitoring-api
- collection_type: open
  name: Socure Account Intelligence Transactions API
  slug: open-socure-transactions-api
- collection_type: open
  name: Socure Account Intelligence Uploads API
  slug: open-socure-uploads-api
- collection_type: open
  name: Socure Global Watchlist Monitoring API
  slug: open-socure-watchlist-monitoring-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/socure-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/socure-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/socure-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/socure-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/socure/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socure-bank-account-onboarding-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socure-contact-risk-then-decision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socure-docv-then-identity-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socure-docv-verify-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socure-fraud-device-risk-screen-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socure-identity-decision-branch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socure-kyc-watchlist-enroll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socure-monitoring-offboard-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socure-watchlist-alert-triage-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.socure.com
- group: start
  title: ''
  type: Portal
  url: https://developer.socure.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.socure.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://developer.socure.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.socure.com/docs/id-plus/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.socure.com/docs/id-plus/getting-started/quick-start-guide
- group: auth
  title: ''
  type: Authentication
  url: https://developer.socure.com/reference/authentication
- group: other
  title: ''
  type: ProductsPage
  url: https://www.socure.com/products
- group: commercial
  title: ''
  type: Pricing
  url: https://www.socure.com/pricing
- group: company
  title: ''
  type: AboutUs
  url: https://www.socure.com/company/about
- group: operate
  title: ''
  type: ContactUs
  url: https://www.socure.com/company/contact
- group: company
  title: ''
  type: Blog
  url: https://www.socure.com/blog
- group: company
  title: ''
  type: Blog
  url: https://www.socure.com/news
- group: other
  title: ''
  type: ResourceCenter
  url: https://www.socure.com/resources
- group: other
  title: ''
  type: CaseStudies
  url: https://www.socure.com/customers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.socure.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.socure.com/legal/terms
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.socure.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.socure.com
- group: company
  title: ''
  type: Careers
  url: https://www.socure.com/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/socure-inc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/socure-inc/socure-docv-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/socure-inc/socure-docv-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/socure-inc/socure-docv-demo-app-react-native
- group: build
  title: ''
  type: SDKs
  url: https://github.com/socure-inc/socure-sigmadevice-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/socure-inc/socure-sigmadevice-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/socure-inc/socure-sigmadevice-demo-app-react-native
- group: build
  title: ''
  type: Tools
  url: https://github.com/socure-inc/riskos-integration-skill
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/socure-inc-
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/socure
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Socure
- group: design
  title: ''
  type: Webhooks
  url: https://developer.socure.com/docs/webhooks/docv-events
- group: operate
  title: ''
  type: Support
  url: https://help.socure.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.socure.com/riskos/docs
- group: docs
  title: ''
  type: Documentation
  url: https://developer.socure.us
- group: commercial
  title: ''
  type: Plans
  url: plans/socure-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/socure-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/socure-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/socure-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/socure-rules.yml
created: '2026-05-25'
description: Socure is the leading vertically-integrated digital identity verification and fraud-prevention platform, used by 3,000+ banks, fintechs, crypto exchanges, marketplaces, gaming operators, and public-sector agencies. The ID+ API exposes Socure's KYC, document verification (DocV), Sigma fraud models, RiskScore (email / phone / address), Global Watchlist screening, Deceased Check, eCBSV, Digital Intelligence (SigmaDevice), Graph Intelligence, Account Intelligence, Prefill, and Decision modules through a single multi-module REST call, complemented by the RiskOS orchestration platform, native mobile SDKs, and webhook event streams. Socure is headquartered in Incline Village, Nevada with origins in New York City.
examples:
- key_count: 2
  name: Socure Docv Create Transaction Example
  slug: socure-docv-create-transaction-example
- key_count: 5
  name: Socure Docv Webhook Example
  slug: socure-docv-webhook-example
- key_count: 2
  name: Socure Idplus Kyc Example
  slug: socure-idplus-kyc-example
features:
- Vertically integrated digital identity verification and fraud prevention platform
- ID+ unified multi-module REST API — pass `modules` array in one request to combine KYC, fraud, risk, and document verification
- Socure Verify (KYC) with industry-leading auto-approval rates and inclusive coverage
- Sigma Identity Fraud, Sigma Synthetic Fraud, and Sigma First-Party Fraud risk scores
- Email RiskScore, Phone RiskScore, and Address RiskScore for low-friction risk signals
- Predictive DocV with biometric face match, liveness detection, and webhook-driven session lifecycle
- Global Watchlist Screening with continuous Monitoring across OFAC, UN, EU, HMT, DFAT, PEP, and adverse media
- Deceased Check against SSA Death Master File and proprietary deceased records
- eCBSV — instant electronic Consent Based SSN Verification with the Social Security Administration
- Digital Intelligence (SigmaDevice SDK) for device fingerprinting and behavioral biometrics
- Graph Intelligence — Network Identity Graph features surfaced as request-time attributes
- Account Intelligence — bank account ownership and status verification
- Prefill — SSN/ITIN autofill to reduce onboarding friction
- Decision module — deterministic rule-based accept/reject/review/refer/resubmit outcomes
- RiskOS orchestration platform (Enterprise and Launch deployment models)
- Native iOS, Android, Web, and React Native SDKs for DocV and SigmaDevice
- Webhook event streams for DocV session lifecycle and Watchlist Monitoring alerts
- SOC 2 Type II, ISO 27001, PCI-DSS, and US FedRAMP-aligned GovCloud environment (developer.socure.us)
- Available globally with country-specific coverage across US, Canada, UK, EU, and LATAM
finops:
- name: Socure Finops
  service_category: ''
  slug: socure-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/socure.png
json_schemas:
- name: Socure ID+ Request
  property_count: 18
  slug: socure-idplus-request
- name: Socure ID+ Response
  property_count: 9
  slug: socure-idplus-response
json_structures:
- name: Socure Idplus Structure
  property_count: 0
  slug: socure-idplus-structure
jsonld:
- class_count: 32
  name: Socure Context
  property_count: 2
  slug: socure-context
layout: provider
modified: '2026-05-25'
name: socure
nav: Providers
network: true
overview: 'socure publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, ID+ API, Monitoring API, and 2 more.


  The socure catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  socure''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, tooling, and 47 more developer resources.'
plans:
- name: Socure Plans Pricing
  plan_count: 3
  slug: socure-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Socure Rate Limits
  slug: socure-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: socure API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: socure-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: socure API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: socure-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: socure API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: socure-rules
score:
  band: strong
  composite: 64.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 30.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 28.8
    contract_quality: 71.7
    developer_ergonomics: 66.7
    discoverability: 63.0
    governance: 28.8
    operational_transparency: 60.5
  previous_composite: 64.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/socure/refs/heads/main/screenshots/socure-2026-06-20T194123.png
security:
- kind: authentication
  name: Socure Authentication
  slug: socure-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Socure Domain Security
  slug: socure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Socure Vulnerability Disclosure
  slug: socure-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: socure
website: https://www.socure.com
---
