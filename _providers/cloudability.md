---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 7
apis:
- description: The Cloudability v3 API is the modern REST interface for the platform. It exposes resource-oriented endpoints for reporting, dimensions and metrics, business mappings, anomalies, rightsizing recommend
  name: Cloudability API v3
  slug: api-v3
- description: The legacy v1 API remains available for older integrations covering cost reporting and dimensions. Apptio recommends migrating to v3 for new integrations. v1 uses an api_key query parameter for authen
  name: Cloudability API v1 (Legacy)
  slug: api-v1
- description: The Reporting endpoints under v3 build cost-and-usage queries against Cloudability's normalized billing dataset. Callers select metrics (unblended cost, amortized cost, usage_quantity), dimensions (ve
  name: Cloudability Reporting API
  slug: reporting
- description: 'Business Mappings define rule-based dimensions that allocate spend to cost centers, products, environments, or applications. The API lets callers list, create, update and delete mappings, manage rule '
  name: Cloudability Business Mappings API
  slug: business-mappings
- description: The Rightsizing API surfaces machine-learning generated downsizing, modernization and termination recommendations for AWS EC2, RDS, EBS, Azure VMs and disks, and Google Compute Engine instances, inclu
  name: Cloudability Rightsizing Recommendations API
  slug: rightsizing
- description: The Anomalies API exposes detected cost anomalies on dimensions such as service, account, and business mapping. Callers can query open anomalies, retrieve baseline / actual cost deltas, classify anoma
  name: Cloudability Anomaly Detection API
  slug: anomalies
- description: The Vendor Credentials API manages connections to AWS payer accounts, Azure billing scopes, GCP billing projects, OCI tenancies and other cloud vendors. It supports listing existing credentials, valid
  name: Cloudability Vendor Credentials API
  slug: vendor-credentials
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudability-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apptio.com/products/cloudability/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cloudability
- group: learn
  title: ''
  type: Training
  url: https://education.apptio.com/courses/ibm-cloudability-api
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudability-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudability-rules.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ibm.com/docs/en/cloudability-commercial
- group: docs
  title: ''
  type: APIReference
  url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas?topic=cloudability-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas?topic=api-getting-started-cloudability-v3
- group: build
  title: ''
  type: Postman
  url: https://github.com/IBM/Apptio-Tools/tree/main/cloudability/postman-collection
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudability
- group: operate
  title: ''
  type: Support
  url: https://www.ibm.com/support/pages/node/7032143
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.ibm.com/community/user/groups/community-home?CommunityKey=15c0e07d-35c0-49de-a84b-019253d13376
- group: company
  title: ''
  type: Blog
  url: https://www.apptio.com/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://automation-management.ideas.ibm.com/?project=CLOUDY
- group: start
  title: ''
  type: SignUp
  url: https://frontdoor.apptio.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ibm.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apptio.com/company/data-privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudability.com/
- group: build
  title: ''
  type: Packages
  url: packages/cloudability-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cloudability-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cloudability-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cloudability-security.txt
- group: auth
  title: ''
  type: Security
  url: security/cloudability-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudability-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudability-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/cloudability-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudability-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudability-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudability-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudability-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudability-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cloudability-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cloudability-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudability-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudability-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cloudability-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudability-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cloudability-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloudability-data-model.yml
created: '2026-03-27'
description: Cloudability (an IBM Apptio product) is a cloud cost management and FinOps platform providing cost visibility, optimization recommendations, anomaly detection, and governance across AWS, Azure, Google Cloud, and other multi-cloud environments. The Cloudability API v3 is REST-oriented with JSON responses, HTTP basic authentication using an API token, cursor-style limit/offset pagination, and operations for reporting, business mappings, rightsizing recommendations, anomalies, vendor credentials, and views.
finops:
- name: Cloudability Finops
  service_category: API
  slug: cloudability-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudability.png
jsonld:
- class_count: 0
  name: Cloudability Context
  property_count: 7
  slug: cloudability-context
layout: provider
modified: '2026-09-05'
name: Cloudability
nav: Providers
network: true
overview: 'Cloudability publishes 1 API on the [APIs.io](https://apis.io/) network: API v3. Tagged areas include Cloud Cost Management, Cost Optimization, FinOps, Multi-Cloud, and Recommendations.


  The Cloudability catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudability''s developer surface includes documentation, GitHub presence, training material, API reference, getting-started guide, support, engineering blog, and 34 more developer resources.'
plans:
- name: Cloudability Plans Pricing
  plan_count: 0
  slug: cloudability-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Cloudability Rate Limits
  slug: cloudability-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Cloudability API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 6
  slug: cloudability-rules
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 66.0
    catalog_earned_first_party: 0.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 24.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 72.7
    contract_quality: 6.7
    developer_ergonomics: 69.0
    discoverability: 74.1
    governance: 72.7
    operational_transparency: 57.9
  previous_composite: 26.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudability/refs/heads/main/screenshots/cloudability-2026-06-20T174542.png
security:
- kind: authentication
  name: Cloudability Authentication
  slug: cloudability-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cloudability Domain Security
  slug: cloudability-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudability Vulnerability Disclosure
  slug: cloudability-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Cloudability Trust Center
  slug: cloudability-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2013, FedRAMP, Cloud Security Alliance STAR Level One, EU GDPR, CCPA, EU-US Privacy Shield
slug: cloudability
tags:
- Cloud Cost Management
- Cost Optimization
- FinOps
- Multi-Cloud
- Recommendations
- Reporting
website: https://www.apptio.com/products/cloudability/
---
