---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazon Vpn Agentic Access
  operation_count: 1
  slug: amazon-vpn-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The AWS VPN API (part of the Amazon EC2 API) provides programmatic access to create and manage VPN connections, customer gateways, virtual private gateways, and Client VPN endpoints. It enables config
  name: AWS VPN API
  slug: aws-vpn-api
- baseURL: https://ec2.amazonaws.com
  baseurl_source: declared
  description: The AWS VPN API (Amazon EC2 Query API Subset) API from Amazon VPN — 1 operation(s) for aws vpn api (amazon ec2 query api subset).
  name: Amazon VPN AWS VPN API (Amazon EC2 Query API Subset) API
  slug: amazon-vpn-aws-vpn-api-amazon-ec2-query-api-subset-api
artifact_total: 21
asyncapis:
- description: ''
  name: Amazon Vpn Events
  slug: amazon-vpn-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS VPN API (Amazon EC2 Query API subset) AWS VPN API (Amazon EC2 Query API Subset) AWS VPN API (Amazon EC2 Query API Subset) AWS VPN API (Amazon EC2 Query API Subset) API
  slug: open-amazon-vpn-aws-vpn-api-amazon-ec2-query-api-subset-api
- collection_type: open
  name: AWS VPN API (Amazon EC2 Query API subset)
  slug: open-amazon-vpn
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-vpn-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-vpn-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-vpn-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-vpn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-vpn-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-vpn-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/vpn/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/vpn/latest/s2svpn/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/vpc/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-vpn/refs/heads/main/rules/amazon-vpn-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-vpn/refs/heads/main/vocabulary/amazon-vpn-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-vpn-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/amazon-vpn-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-vpn-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-vpn-security.txt
- group: auth
  title: ''
  type: Security
  url: https://vdp.aws.security/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/programs/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-vpn-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/amazon-vpn-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-vpn-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-vpn-aws-vpn-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-vpn-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-vpn-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-vpn-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amazon-vpn-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/amazon-vpn-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amazon-vpn-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/amazon-vpn-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amazon-vpn-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: EventCatalog
  url: asyncapi/amazon-vpn-events.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amazon-vpn-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amazon-vpn-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/amazon-vpn-finops.yml
- group: build
  title: ''
  type: Examples
  url: examples/amazon-vpn-example.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/amazon-vpn-context.jsonld
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Operations.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/vpn/pricing/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/networking-and-content-delivery/
created: '2026-03-16'
description: 'AWS VPN solutions establish secure connections between on-premises networks, remote offices, client devices, and the AWS global network. AWS offers two types of private connectivity: AWS Site-to-Site VPN and AWS Client VPN, enabling encrypted tunnels between your network and Amazon Virtual Private Cloud.'
examples:
- key_count: 2
  name: Amazon Vpn Example
  slug: amazon-vpn-example
features:
- description: Automate operational tasks with Amazon VPN.
  name: Automation
- description: Programmatic access to Amazon VPN resources.
  name: API Access
finops:
- name: Amazon Vpn Finops
  service_category: API
  slug: amazon-vpn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-vpn.png
jsonld:
- class_count: 0
  name: Amazon Vpn Context
  property_count: 0
  slug: amazon-vpn-context
layout: provider
mcp_servers:
- description: ''
  name: AWS MCP servers reaching the VPN surface
  slug: aws-mcp-servers-reaching-the-vpn-surface
modified: '2026-09-01'
name: Amazon VPN
nav: Providers
network: true
overview: 'Amazon VPN publishes 1 API on the [APIs.io](https://apis.io/) network: AWS VPN API (Amazon EC2 Query API Subset) API. Tagged areas include Networking, Security, VPN, IPsec, and Hybrid Cloud.


  The Amazon VPN catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Amazon VPN''s developer surface includes authentication, developer portal, documentation, developer console, support, signup flow, changelog, and 41 more developer resources.'
plans:
- name: Amazon Vpn Plans Pricing
  plan_count: 5
  slug: amazon-vpn-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 7
  name: Amazon Vpn Rate Limits
  slug: amazon-vpn-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Amazon VPN API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 7
  slug: amazon-vpn-spectral-rules
score:
  band: exemplar
  composite: 74.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 77.8
    catalog_earned_first_party: 24.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 44.7
    contract_quality: 71.1
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 44.7
    operational_transparency: 65.8
  previous_composite: 74.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-vpn/refs/heads/main/screenshots/amazon-vpn-2026-06-20T171844.png
security:
- kind: authentication
  name: Amazon Vpn Authentication
  slug: amazon-vpn-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Vpn Domain Security
  slug: amazon-vpn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Vpn Vulnerability Disclosure
  slug: amazon-vpn-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Amazon Vpn Trust Center
  slug: amazon-vpn-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-vpn
tags:
- Networking
- Security
- VPN
- IPsec
- Hybrid Cloud
- Connectivity
- Infrastructure
use_cases:
- description: Use Amazon VPN to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/vpn/
---
