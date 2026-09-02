---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 69
  human_in_the_loop: 0
  name: Alloy Com Agentic Access
  operation_count: 115
  slug: alloy-com-agentic-access
  summary_line: 115 operations · 69 acting
api_count: 2
apis:
- description: Bank account records and related entity history.
  name: Alloy Bank Accounts API
  slug: alloy-com-bank-accounts-api
- description: Batch processing of journey applications and evaluations.
  name: Alloy Batches API
  slug: alloy-com-batches-api
- description: Case management, evidences, and review work items.
  name: Alloy Cases API
  slug: alloy-com-cases-api
- description: Tenant-defined reference lists with versioning and activation.
  name: Alloy Custom Lists API
  slug: alloy-com-custom-lists-api
- description: Uploaded identity, address, and supporting documents for entities.
  name: Alloy Documents API
  slug: alloy-com-documents-api
- description: Person and business entities, notes, merging, feedback, and groups.
  name: Alloy Entities API
  slug: alloy-com-entities-api
- description: Run, retrieve, and audit identity, KYC, KYB, AML, fraud, and credit evaluations.
  name: Alloy Evaluations API
  slug: alloy-com-evaluations-api
- description: Real-time monitoring events for entities, accounts, transactions, and logins.
  name: Alloy Events API
  slug: alloy-com-events-api
- description: Entity groups and group-level evaluations.
  name: Alloy Groups API
  slug: alloy-com-groups-api
- description: Investigation lifecycle, assignment, review, archival, and types.
  name: Alloy Investigations API
  slug: alloy-com-investigations-api
- description: Multi-step decisioning journeys, applications, batches, and reviews.
  name: Alloy Journeys API
  slug: alloy-com-journeys-api
- description: Built-in watchlist-style lists and list metadata.
  name: Alloy Lists API
  slug: alloy-com-lists-api
- description: OAuth 2.0 bearer token issuance and validation.
  name: Alloy OAuth API
  slug: alloy-com-oauth-api
- description: Tenant-level parameters for evaluations and journeys.
  name: Alloy Parameters API
  slug: alloy-com-parameters-api
- description: Bulk re-evaluations across a portfolio of entities.
  name: Alloy Portfolio Evaluations API
  slug: alloy-com-portfolio-evaluations-api
- description: Custom attributes published from external systems and used in policy.
  name: Alloy Published Attributes API
  slug: alloy-com-published-attributes-api
- description: Manual review notes and decisions on entities.
  name: Alloy Reviews API
  slug: alloy-com-reviews-api
- description: Entity groups can be used to associate multiple Person and Business Entities together at the point of onboarding and update throughout the entity lifecycle.
  name: Alloy Entity Groups API
  slug: alloy-com-entity-groups-api
- description: Manage transactions. These transactions are aggregated and decisioned through Transaction Monitoring workflows and evaluations.
  name: Alloy Transactions API
  slug: alloy-com-transactions-api
artifact_total: 86
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Alloy Bank Accounts API
  slug: open-alloy-com-bank-accounts-api
- collection_type: open
  name: Alloy Bank Accounts Batches API
  slug: open-alloy-com-batches-api
- collection_type: open
  name: Alloy Bank Accounts Cases API
  slug: open-alloy-com-cases-api
- collection_type: open
  name: Alloy Bank Accounts Custom Lists API
  slug: open-alloy-com-custom-lists-api
- collection_type: open
  name: Alloy Bank Accounts Documents API
  slug: open-alloy-com-documents-api
- collection_type: open
  name: Alloy Bank Accounts Entities API
  slug: open-alloy-com-entities-api
- collection_type: open
  name: Alloy Identity Bank Accounts Entity Groups API
  slug: open-alloy-com-entity-groups-api
- collection_type: open
  name: Alloy Bank Accounts Evaluations API
  slug: open-alloy-com-evaluations-api
- collection_type: open
  name: Alloy Bank Accounts Events API
  slug: open-alloy-com-events-api
- collection_type: open
  name: Alloy Bank Accounts Groups API
  slug: open-alloy-com-groups-api
- collection_type: open
  name: Alloy Bank Accounts Investigations API
  slug: open-alloy-com-investigations-api
- collection_type: open
  name: Alloy Bank Accounts Journeys API
  slug: open-alloy-com-journeys-api
- collection_type: open
  name: Alloy Bank Accounts Lists API
  slug: open-alloy-com-lists-api
- collection_type: open
  name: Alloy Bank Accounts OAuth API
  slug: open-alloy-com-oauth-api
- collection_type: open
  name: Alloy Bank Accounts Parameters API
  slug: open-alloy-com-parameters-api
- collection_type: open
  name: Alloy Bank Accounts Portfolio Evaluations API
  slug: open-alloy-com-portfolio-evaluations-api
- collection_type: open
  name: Alloy Bank Accounts Published Attributes API
  slug: open-alloy-com-published-attributes-api
- collection_type: open
  name: Alloy Identity Bank Accounts Transactions API
  slug: open-alloy-com-transactions-api
- collection_type: open
  name: Alloy API
  slug: open-alloy
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/alloy-com-capability-edges.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.alloy.com/public/docs/getting-started
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alloy-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alloy-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alloy-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.alloy.com/
- group: start
  title: ''
  type: Portal
  url: https://www.alloy.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://developer.alloy.com/public/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.alloy.com/public/reference
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.alloy.com/llms.txt
- group: start
  title: ''
  type: Login
  url: https://app.alloy.co/login/
- group: start
  title: ''
  type: Signup
  url: https://www.alloy.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alloy.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alloy.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alloy.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.alloy.com/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alloy.com/
- group: operate
  title: ''
  type: Support
  url: https://help.alloy.com
- group: company
  title: ''
  type: Blog
  url: https://www.alloy.com/blog
- group: build
  title: ''
  type: ContentLibrary
  url: https://www.alloy.com/content-library
- group: learn
  title: ''
  type: Training
  url: https://alloy.docebosaas.com/learn/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UseAlloy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alloy/
- group: commercial
  title: ''
  type: Plans
  url: plans/alloy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alloy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alloy-finops.yml
- group: auth
  title: ''
  type: Certifications
  url: ''
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alloy-com-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.alloy.com/developer
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/useAlloy
- group: operate
  title: ''
  type: StatusPageAlt
  url: https://alloy.statuspage.io
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.alloy.com/hc/en-us
- group: other
  title: ''
  type: X
  url: https://x.com/usealloy
created: '2026-05-25'
description: Alloy is a New York-based identity decisioning platform that helps banks, credit unions, and fintechs onboard, monitor, and protect customers across KYC, KYB, AML, fraud, credit, and ongoing-monitoring use cases. The Alloy API exposes the platform's evaluations, journey applications, entities, events, documents, cases, investigations, lists, and webhooks for programmatic identity decisioning and ongoing risk monitoring.
examples:
- key_count: 8
  name: Alloy Com Evaluation Response
  slug: alloy-com-evaluation-response
- key_count: 2
  name: Alloy Com Event Request
  slug: alloy-com-event-request
- key_count: 7
  name: Alloy Com Journey Application Request
  slug: alloy-com-journey-application-request
- key_count: 7
  name: Alloy Com Person Evaluation Request
  slug: alloy-com-person-evaluation-request
features:
- description: Verify person and business identities against 270+ data sources across 195 markets.
  name: Identity
- description: Configurable Journeys orchestrate KYC, KYB, document verification, and step-up review for new customer acquisition.
  name: Onboarding
- description: Perpetual KYC and event-driven monitoring across logins, credential updates, transactions, and account changes.
  name: Ongoing Monitoring
- description: Machine-learning Fraud Signal and integrated device-risk providers detect fraud across onboarding and post-onboarding events.
  name: Fraud
- description: Credit underwriting and policy management with Journey- based decisioning.
  name: Credit
- description: Cases, evidences, and works support compliance review and dispute workflows.
  name: Case Management
- description: Investigation lifecycle with alerts tied to journey applications and assignable agents.
  name: Investigations
- description: Bring custom ML models and published attributes into Alloy workflows for tenant-specific decisioning logic.
  name: Custom Models and Attributes
- description: Real-time notifications for journey, case, and investigation events with Basic, HMAC, and OAuth 2.0 auth.
  name: Webhooks
- description: Web, iOS Webview, and Android Webview SDKs for embedding Alloy's document verification and step-up flows.
  name: SDKs
finops:
- name: Alloy Com Finops
  service_category: ''
  slug: alloy-com-finops
- name: Alloy Finops
  service_category: API
  slug: alloy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alloy-com.png
integrations:
- description: Digital identity and device intelligence integration.
  name: Socure
- description: Device risk and fraud signals integration.
  name: Experian FraudNet
- description: Device risk integration.
  name: TruValidate (Iovation)
- description: Behavioral risk integration.
  name: NeuroID
- description: Behavioral biometrics integration.
  name: BioCatch
- description: Device risk and fraud signals integration.
  name: ThreatMetrix
- description: Identity provider integrations for Okta, Azure AD, ADFS, JumpCloud, and generic SAML 2.0.
  name: SAML SSO
- description: User provisioning integrations for Okta and Azure.
  name: SCIM
json_schemas:
- name: Alloy Business Entity
  property_count: 11
  slug: alloy-com-business-entity
- name: Alloy Entity
  property_count: 13
  slug: alloy-com-entity
- name: Alloy Evaluation
  property_count: 8
  slug: alloy-com-evaluation
jsonld:
- class_count: 24
  name: Alloy Com Context
  property_count: 46
  slug: alloy-com-context
layout: provider
modified: '2026-08-08'
name: Alloy
nav: Providers
network: true
overview: 'Alloy publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Bank Accounts API, Batches API, Cases API, and 16 more. Tagged areas include Identity Decisioning, Identity Verification, KYC, KYB, and AML.


  The Alloy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Alloy''s developer surface includes getting-started guide, authentication, developer portal, documentation, API reference, signup flow, pricing, and 25 more developer resources.'
plans:
- name: Alloy Com Plans Pricing
  plan_count: 1
  slug: alloy-com-plans-pricing
- name: Alloy Plans Pricing
  plan_count: 2
  slug: alloy-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Alloy Com Rate Limits
  slug: alloy-com-rate-limits
- limit_count: 3
  name: Alloy Rate Limits
  slug: alloy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Alloy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: alloy-com-jsonschema-spectral-rules
scopes:
- name: Alloy Com Scopes
  scope_count: 0
  slug: alloy-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 9.8
    contract_quality: 53.2
    developer_ergonomics: 73.8
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 58.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alloy-com/refs/heads/main/screenshots/alloy-com-2026-06-20T171540.png
security:
- kind: authentication
  name: Alloy Com Authentication
  slug: alloy-com-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Alloy Com Domain Security
  slug: alloy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: alloy-com
solutions:
- description: Identity and fraud platform for traditional financial institutions.
  name: Banks and Credit Unions
- description: Onboarding and risk platform for consumer and business fintechs.
  name: Fintechs
- description: Embedded finance program risk management for sponsor banks supporting fintech programs.
  name: Sponsor Banks
tags:
- Identity Decisioning
- Identity Verification
- KYC
- KYB
- AML
- Fraud Prevention
- Credit Underwriting
- Ongoing Monitoring
- Case Management
- Fintech
- Banking
use_cases:
- description: Verify individual consumers during account opening for banks, neobanks, and consumer fintechs.
  name: Consumer Onboarding (KYC)
- description: Verify businesses and beneficial owners for SMB banking, payments, and lending products.
  name: Business Onboarding (KYB)
- description: Screen against sanctions, PEP, and adverse-media lists and monitor ongoing activity for AML risk.
  name: AML Compliance
- description: Detect synthetic identity, account takeover, and transaction fraud across onboarding and post-onboarding.
  name: Fraud Prevention
- description: Run credit decisioning Journeys for lending and BNPL products.
  name: Credit Underwriting
- description: Sponsor banks orchestrate fintech program risk through configurable Journeys and ongoing monitoring.
  name: Embedded Finance Risk
- description: Continuously re-evaluate customers against fresh data using ongoing monitoring events.
  name: Perpetual KYC
website: https://www.alloy.com/
---
