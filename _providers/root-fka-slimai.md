---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Root Fka Slimai Agentic Access
  operation_count: 69
  slug: root-fka-slimai-agentic-access
  summary_line: 69 operations · 31 acting
api_count: 20
apis:
- description: The Accounts API from Root (fka Slim.ai) — 3 operation(s) for accounts.
  name: Root (fka Slim.ai) Accounts API
  slug: root-fka-slimai-accounts-api
- description: The API Keys API from Root (fka Slim.ai) — 2 operation(s) for api keys.
  name: Root (fka Slim.ai) API Keys API
  slug: root-fka-slimai-api-keys-api
- description: The Authentication API from Root (fka Slim.ai) — 1 operation(s) for authentication.
  name: Root (fka Slim.ai) Authentication API
  slug: root-fka-slimai-authentication-api
- description: The AVR API from Root (fka Slim.ai) — 6 operation(s) for avr.
  name: Root (fka Slim.ai) AVR API
  slug: root-fka-slimai-avr-api
- description: The Billing API from Root (fka Slim.ai) — 1 operation(s) for billing.
  name: Root (fka Slim.ai) Billing API
  slug: root-fka-slimai-billing-api
- description: The Core - Discovered Packages V3 API from Root (fka Slim.ai) — 1 operation(s) for core - discovered packages v3.
  name: Root (fka Slim.ai) Core - Discovered Packages V3 API
  slug: root-fka-slimai-core-discovered-packages-v3-api
- description: The CveFeed API from Root (fka Slim.ai) — 1 operation(s) for cvefeed.
  name: Root (fka Slim.ai) CveFeed API
  slug: root-fka-slimai-cvefeed-api
- description: The Discovery API from Root (fka Slim.ai) — 2 operation(s) for discovery.
  name: Root (fka Slim.ai) Discovery API
  slug: root-fka-slimai-discovery-api
- description: The Invitations API from Root (fka Slim.ai) — 3 operation(s) for invitations.
  name: Root (fka Slim.ai) Invitations API
  slug: root-fka-slimai-invitations-api
- description: The Notifications API from Root (fka Slim.ai) — 4 operation(s) for notifications.
  name: Root (fka Slim.ai) Notifications API
  slug: root-fka-slimai-notifications-api
- description: The Organizations API from Root (fka Slim.ai) — 1 operation(s) for organizations.
  name: Root (fka Slim.ai) Organizations API
  slug: root-fka-slimai-organizations-api
- description: The OSVFeed API from Root (fka Slim.ai) — 3 operation(s) for osvfeed.
  name: Root (fka Slim.ai) OSVFeed API
  slug: root-fka-slimai-osvfeed-api
- description: The Package API from Root (fka Slim.ai) — 4 operation(s) for package.
  name: Root (fka Slim.ai) Package API
  slug: root-fka-slimai-package-api
- description: The Patches API from Root (fka Slim.ai) — 3 operation(s) for patches.
  name: Root (fka Slim.ai) Patches API
  slug: root-fka-slimai-patches-api
- description: The PatchFeed API from Root (fka Slim.ai) — 1 operation(s) for patchfeed.
  name: Root (fka Slim.ai) PatchFeed API
  slug: root-fka-slimai-patchfeed-api
- description: The Remediation API from Root (fka Slim.ai) — 10 operation(s) for remediation.
  name: Root (fka Slim.ai) Remediation API
  slug: root-fka-slimai-remediation-api
- description: The Security Findings API from Root (fka Slim.ai) — 4 operation(s) for security findings.
  name: Root (fka Slim.ai) Security Findings API
  slug: root-fka-slimai-security-findings-api
- description: The Subscriptions API from Root (fka Slim.ai) — 2 operation(s) for subscriptions.
  name: Root (fka Slim.ai) Subscriptions API
  slug: root-fka-slimai-subscriptions-api
- description: The System Matrix API from Root (fka Slim.ai) — 2 operation(s) for system matrix.
  name: Root (fka Slim.ai) System Matrix API
  slug: root-fka-slimai-system-matrix-api
- description: The Webhooks API from Root (fka Slim.ai) — 3 operation(s) for webhooks.
  name: Root (fka Slim.ai) Webhooks API
  slug: root-fka-slimai-webhooks-api
artifact_total: 27
asyncapis:
- description: ''
  name: Root Fka Slimai Webhooks
  slug: root-fka-slimai-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/root-fka-slimai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/root-fka-slimai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/root-fka-slimai-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/root-fka-slimai-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/root-fka-slimai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/root-fka-slimai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/root-fka-slimai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.root.io/compliance/certifications
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/root-fka-slimai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/root-fka-slimai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/root-fka-slimai-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/root-fka-slimai-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/root-fka-slimai-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/root-fka-slimai-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/root-fka-slimai-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/root-fka-slimai-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/root-fka-slimai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.root.io/compliance/security-posture
- group: auth
  title: ''
  type: TrustCenter
  url: security/root-fka-slimai-trust-center.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.root.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.root.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.root.io/quickstart
- group: operate
  title: ''
  type: Support
  url: https://start-chat.com/slack/Root/ghdO0t
- group: company
  title: ''
  type: Blog
  url: https://www.root.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rootio-avr
- group: start
  title: ''
  type: SignUp
  url: https://app.root.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.root.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.root.io/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.root.io/
created: '2026-07-17'
description: 'Root (formerly Slim.ai) is a container and dependency security company backed by Insight Partners. Its "secure supply" platform delivers end-to-end, autonomous vulnerability remediation for container images and application packages: a fleet of AI agents (Agentic Vulnerability Remediation, AVR) researches, patches, tests, and ships Root Patches within minutes of CVE publication, without base-image changes or forced version upgrades. Root operates the Root Image Catalog (cr.root.io), Library Catalog, and OS-package registry (pkg.root.io), and exposes a REST API (api.root.io) for querying patch status, security findings, subscriptions, and pulling SBOM, VEX, and provenance artifacts, plus Standard-Webhooks notifications and a first-party CLI (rootio_patcher).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/root-fka-slimai.png
layout: provider
mcp_servers:
- description: ''
  name: root-fka-slimai-mcp.yml
  slug: root-fka-slimai-mcpyml
modified: '2026-07-21'
name: Root (fka Slim.ai)
nav: Providers
network: true
overview: 'Root (fka Slim.ai) publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, API Keys API, Authentication API, and 17 more. Tagged areas include Company, Security, Vulnerability Management, Container Security, and DevSecOps.


  The Root (fka Slim.ai) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Root (fka Slim.ai)''s developer surface includes authentication, changelog, CLI, documentation, getting-started guide, support, engineering blog, and 23 more developer resources.'
random_paper: 29
score:
  band: developing
  composite: 49.9
  delta: -3.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Root Fka Slimai Authentication
  slug: root-fka-slimai-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Root Fka Slimai Domain Security
  slug: root-fka-slimai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Root Fka Slimai Vulnerability Disclosure
  slug: root-fka-slimai-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Root Fka Slimai Trust Center
  slug: root-fka-slimai-trust-center
  summary_line: SOC 2 Type II, Cyber Essentials, SLSA, FIPS 140-3, STIG
slug: root-fka-slimai
tags:
- Company
- Security
- Vulnerability Management
- Container Security
- DevSecOps
- Software Supply Chain
- CVE
- SBOM
- Open Source
- Patching
website: https://www.root.io/
---
