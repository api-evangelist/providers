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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Emailrep Agentic Access
  operation_count: 2
  slug: emailrep-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: Report email addresses as malicious so the reputation graph picks up the signal.
  name: EmailRep Reports API
  slug: emailrep-reports-api
- description: Query email address reputation and threat-intelligence signals.
  name: EmailRep Reputation API
  slug: emailrep-reputation-api
arazzos:
- description: Query an email's reputation and, when the signals show it is malicious, report it back into the reputation graph.
  name: EmailRep Screen and Report Malicious Sender
  slug: emailrep-screen-and-report-malicious-workflow
- description: Pull a human-readable reputation summary for an inbound sender and escalate low-reputation, spoofable senders by reporting them.
  name: EmailRep Triage Inbound Sender
  slug: emailrep-triage-inbound-sender-workflow
- description: Confirm an email's domain resolves and is deliverable before reporting it, so junk addresses never pollute the reputation graph.
  name: EmailRep Verify Before Report
  slug: emailrep-verify-before-report-workflow
artifact_total: 28
collections:
- collection_type: postman
  name: EmailRep API
  slug: postman-emailrep-api
- collection_type: open
  name: EmailRep API
  slug: open-emailrep-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emailrep-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emailrep-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/emailrep-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/emailrep/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emailrep-screen-and-report-malicious-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emailrep-triage-inbound-sender-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emailrep-verify-before-report-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://emailrep.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sublimesecurity.com/reference/emailrep-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sublimesecurity.com/reference/emailrep-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sublimesecurity.com/reference/emailrep-quickstart
- group: start
  title: ''
  type: Signup
  url: https://emailrep.io/key
- group: commercial
  title: ''
  type: Pricing
  url: https://emailrep.io/key
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emailrep.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emailrep.io/privacy
- group: company
  title: ''
  type: Blog
  url: https://emailrep.io/blog
- group: operate
  title: ''
  type: Support
  url: https://sublimesecurity.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sublime-security
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/sublime-security/emailrep.io
- group: other
  title: ''
  type: Operator
  url: https://sublimesecurity.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sublime-security
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: Sublime Platform
  type: Tools
  url: https://github.com/sublime-security/sublime-platform
- group: build
  title: Sublime Rules
  type: Tools
  url: https://github.com/sublime-security/sublime-rules
- group: build
  title: Sublime CLI
  type: Tools
  url: https://github.com/sublime-security/sublime-cli
- group: build
  title: OpenCTI Connectors
  type: Tools
  url: https://github.com/sublime-security/connectors
- group: build
  title: MQL VS Code Extension
  type: Tools
  url: https://github.com/sublime-security/mql-vscode
- group: build
  title: ICS Phishing Toolkit
  type: Tools
  url: https://github.com/sublime-security/ics-phishing-toolkit
- group: build
  title: Strelka File Scanning
  type: Tools
  url: https://github.com/sublime-security/strelka
- group: learn
  title: Detection Engineering Workshop
  type: Tutorials
  url: https://github.com/sublime-security/detection-workshop
- group: commercial
  title: ''
  type: Plans
  url: plans/emailrep-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/emailrep-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/emailrep-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/emailrep-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/emailrep-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/api-email-reputation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/api-email-reputation-details-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/api-report-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/api-report-response-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/api-email-reputation-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/api-email-reputation-details-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/api-report-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/api-report-response-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/emailrep-api-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/api-email-reputation-example.json
- group: build
  title: ''
  type: Examples
  url: examples/api-email-reputation-details-example.json
- group: build
  title: ''
  type: Examples
  url: examples/api-report-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/api-report-response-example.json
created: '2026-05-28'
description: EmailRep is an email address reputation and threat-intelligence API operated by Sublime Security, Inc. It crawls and enriches data across social media profiles, professional networking sites, dark-web credential leaks, data breaches, phishing kits, phishing emails, spam lists, open mail relays, spam traps, domain age and reputation, and email-deliverability signals to predict the risk associated with any email address. The free, JSON-over-HTTP REST API returns a `reputation`, a `suspicious` flag, a `references` count, and a detailed signal block (blacklisted, malicious_activity, credentials_leaked, data_breach, domain_reputation, deliverable, spoofable, profiles, and more). A POST `/report` endpoint lets analysts contribute observations of malicious email behavior back into the reputation graph.
examples:
- key_count: 23
  name: Api Email Reputation Details Example
  slug: api-email-reputation-details-example
- key_count: 6
  name: Api Email Reputation Example
  slug: api-email-reputation-example
- key_count: 5
  name: Api Report Request Example
  slug: api-report-request-example
- key_count: 2
  name: Api Report Response Example
  slug: api-report-response-example
finops:
- name: Emailrep Finops
  service_category: Identity + Security + Email Reputation
  slug: emailrep-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emailrep.png
json_schemas:
- name: EmailReputationDetails
  property_count: 23
  slug: api-email-reputation-details
- name: EmailReputation
  property_count: 6
  slug: api-email-reputation
- name: ReportRequest
  property_count: 5
  slug: api-report-request
- name: ReportResponse
  property_count: 2
  slug: api-report-response
json_structures:
- name: Api Email Reputation Details Structure
  property_count: 23
  slug: api-email-reputation-details-structure
- name: Api Email Reputation Structure
  property_count: 6
  slug: api-email-reputation-structure
- name: Api Report Request Structure
  property_count: 5
  slug: api-report-request-structure
- name: Api Report Response Structure
  property_count: 2
  slug: api-report-response-structure
jsonld:
- class_count: 4
  name: Emailrep Api Context
  property_count: 35
  slug: emailrep-api-context
layout: provider
modified: '2026-05-30'
name: EmailRep
nav: Providers
network: true
overview: 'EmailRep publishes 2 APIs on the [APIs.io](https://apis.io/) network: Reports API and Reputation API. Tagged areas include Security, Email, Email Reputation, Threat Intelligence, and Phishing.


  The EmailRep catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  EmailRep''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, and 41 more developer resources.'
plans:
- name: Emailrep Plans Pricing
  plan_count: 3
  slug: emailrep-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Emailrep Rate Limits
  slug: emailrep-rate-limits
rules:
- name: EmailRep API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: emailrep-jsonschema-spectral-rules
- name: EmailRep API Rules
  rule_count: 47
  severity_counts:
    error: 17
    hint: 0
    info: 3
    warn: 27
  slug: emailrep-spectral-rules
score:
  band: strong
  composite: 62.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 69.0
    developer_ergonomics: 47.8
    discoverability: 60.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 62.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emailrep/refs/heads/main/screenshots/emailrep-2026-06-20T180624.png
security:
- kind: authentication
  name: Emailrep Authentication
  slug: emailrep-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Emailrep Domain Security
  slug: emailrep-domain-security
  summary_line: TLSv1.2 · DMARC
slug: emailrep
tags:
- Security
- Email
- Email Reputation
- Threat Intelligence
- Phishing
- Fraud Prevention
- Anti-Abuse
- Deliverability
- Risk Scoring
- Public APIs
website: https://emailrep.io
---
