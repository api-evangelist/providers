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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.3
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Stedi Agentic Access
  operation_count: 75
  slug: stedi-agentic-access
  summary_line: 75 operations · 31 acting
api_count: 21
apis:
- description: The Claim acknowledgments API from Stedi — 1 operation(s) for claim acknowledgments.
  name: Stedi Claim acknowledgments API
  slug: stedi-claim-acknowledgments-api
- description: The Claim Attachments API from Stedi — 2 operation(s) for claim attachments.
  name: Stedi Claim Attachments API
  slug: stedi-claim-attachments-api
- description: The Claim submission API from Stedi — 8 operation(s) for claim submission.
  name: Stedi Claim submission API
  slug: stedi-claim-submission-api
- description: The Coordination of benefits API from Stedi — 1 operation(s) for coordination of benefits.
  name: Stedi Coordination of benefits API
  slug: stedi-coordination-of-benefits-api
- description: The Documents API from Stedi — 2 operation(s) for documents.
  name: Stedi Documents API
  slug: stedi-documents-api
- description: The Enrollments API from Stedi — 4 operation(s) for enrollments.
  name: Stedi Enrollments API
  slug: stedi-enrollments-api
- description: The Events API from Stedi — 3 operation(s) for events.
  name: Stedi Events API
  slug: stedi-events-api
- description: The Executions API from Stedi — 11 operation(s) for executions.
  name: Stedi Executions API
  slug: stedi-executions-api
- description: The Fragments API from Stedi — 1 operation(s) for fragments.
  name: Stedi Fragments API
  slug: stedi-fragments-api
- description: The Insurance discovery API from Stedi — 2 operation(s) for insurance discovery.
  name: Stedi Insurance discovery API
  slug: stedi-insurance-discovery-api
- description: The Partnerships API from Stedi — 3 operation(s) for partnerships.
  name: Stedi Partnerships API
  slug: stedi-partnerships-api
- description: The Payer API from Stedi — 1 operation(s) for payer.
  name: Stedi Payer API
  slug: stedi-payer-api
- description: The Payers API from Stedi — 4 operation(s) for payers.
  name: Stedi Payers API
  slug: stedi-payers-api
- description: The Polling API from Stedi — 2 operation(s) for polling.
  name: Stedi Polling API
  slug: stedi-polling-api
- description: The Providers API from Stedi — 2 operation(s) for providers.
  name: Stedi Providers API
  slug: stedi-providers-api
- description: The Real-time claim status API from Stedi — 2 operation(s) for real-time claim status.
  name: Stedi Real-time claim status API
  slug: stedi-real-time-claim-status-api
- description: The Real-time eligibility check API from Stedi — 2 operation(s) for real-time eligibility check.
  name: Stedi Real-time eligibility check API
  slug: stedi-real-time-eligibility-check-api
- description: The Remittances API from Stedi — 2 operation(s) for remittances.
  name: Stedi Remittances API
  slug: stedi-remittances-api
- description: The Tasks API from Stedi — 1 operation(s) for tasks.
  name: Stedi Tasks API
  slug: stedi-tasks-api
- description: The Transactions API from Stedi — 11 operation(s) for transactions.
  name: Stedi Transactions API
  slug: stedi-transactions-api
- description: The X12 API from Stedi — 1 operation(s) for x12.
  name: Stedi X12 API
  slug: stedi-x12-api
arazzos:
- description: Resolve a claim-status-capable payer, run an X12 276 inquiry, and convert the X12 277 status report.
  name: Stedi X12 276/277 Claim Status Inquiry
  slug: stedi-claim-status-inquiry-workflow
- description: Locate the right payer in the Stedi network, then run an X12 270 eligibility inquiry and read the 271 benefits response.
  name: Stedi X12 270/271 Eligibility and Benefits Check
  slug: stedi-eligibility-check-workflow
- description: Start an insurance discovery check for a patient, then poll until the X12 270/271 coverage search completes and read the discovered coverage.
  name: Stedi Insurance Discovery
  slug: stedi-insurance-discovery-workflow
- description: Submit an X12 837 professional claim, check its 277 status, and retrieve the converted X12 835 remittance.
  name: Stedi X12 837 Professional Claim Lifecycle
  slug: stedi-professional-claim-lifecycle-workflow
- description: Create a provider, open an enrollment, upload the signed agreement, and read the enrollment status for X12 835 ERA/EFT transactions.
  name: Stedi Provider Enrollment for X12 835 ERA/EFT
  slug: stedi-provider-enrollment-workflow
artifact_total: 47
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stedi-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stedi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stedi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stedi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.stedi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.stedi.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stedi
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/Stedi/openApi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stedi-inc
- group: other
  title: ''
  type: X
  url: https://x.com/stedi
- group: company
  title: ''
  type: Blog
  url: https://www.stedi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stedi.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stedi.com
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/stedi-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/stedi-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/stedi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stedi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stedi-finops.yml
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
created: 2026-06-12
description: Stedi is the only API-first programmable healthcare clearinghouse, enabling health tech companies to submit claims, verify eligibility, and process electronic remittance advice (ERA) through a modern JSON API. The platform supports real-time X12 EDI transaction processing including eligibility checks (270/271), professional and institutional claim submissions (837), claim status inquiries (276/277), and electronic remittance advice (835). Stedi provides both SFTP and REST API access, webhooks for event-driven workflows, a sandbox test environment, and an MCP server for AI-assisted integration. Public OpenAPI specifications are available for all core APIs via the Stedi GitHub organization, and pricing is purely metered with no monthly minimums or setup fees.
examples:
- key_count: 4
  name: Stedi Claims Examples
  slug: stedi-claims-examples
- key_count: 35
  name: Stedi Core Examples
  slug: stedi-core-examples
- key_count: 18
  name: Stedi Enrollment Examples
  slug: stedi-enrollment-examples
- key_count: 2
  name: Stedi Event Destinations Examples
  slug: stedi-event-destinations-examples
- key_count: 36
  name: Stedi Healthcare Examples
  slug: stedi-healthcare-examples
- key_count: 4
  name: Stedi Payers Examples
  slug: stedi-payers-examples
finops:
- name: Stedi Finops
  service_category: ''
  slug: stedi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stedi.png
json_schemas:
- name: Stedi Claims Schemas
  property_count: 0
  slug: stedi-claims-schemas
- name: Stedi Core Schemas
  property_count: 0
  slug: stedi-core-schemas
- name: Stedi Enrollment Schemas
  property_count: 0
  slug: stedi-enrollment-schemas
- name: Stedi Event-Destinations Schemas
  property_count: 0
  slug: stedi-event-destinations-schemas
- name: Stedi Healthcare Schemas
  property_count: 0
  slug: stedi-healthcare-schemas
- name: Stedi Payers Schemas
  property_count: 0
  slug: stedi-payers-schemas
jsonld:
- class_count: 854
  name: Stedi Context
  property_count: 0
  slug: stedi-context
layout: provider
modified: 2026-06-12
name: Stedi
nav: Providers
network: true
overview: 'Stedi publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Claim acknowledgments API, Claim Attachments API, Claim submission API, and 18 more. Tagged areas include EDI, Electronic Data Interchange, Healthcare, Clearinghouse, and X12.


  The Stedi catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stedi''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Stedi Plans Pricing
  plan_count: 3
  slug: stedi-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 4
  name: Stedi Rate Limits
  slug: stedi-rate-limits
rules:
- name: Stedi API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: stedi-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.8
  delta: -0.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 62.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 34.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stedi/refs/heads/main/screenshots/stedi-2026-06-20T194534.png
security:
- kind: authentication
  name: Stedi Authentication
  slug: stedi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Stedi Domain Security
  slug: stedi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stedi Vulnerability Disclosure
  slug: stedi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: stedi
tags:
- EDI
- Electronic Data Interchange
- Healthcare
- Clearinghouse
- X12
- Claims
- Eligibility
- HIPAA
- Revenue Cycle Management
- B2B Integration
website: https://www.stedi.com
---
