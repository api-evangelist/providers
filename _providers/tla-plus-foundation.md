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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 2.5
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: TLC is the primary model checker for specifications written in TLA+. It can be run from the command line using tla2tools.jar or consumed as a Java dependency via Maven from central.sonatype.org. Requi
  name: TLC Model Checker
  slug: tlc-model-checker
- description: The TLA+ Proof Manager (TLAPS) is a proof system for TLA+ specifications, enabling formal mathematical proofs of system properties. It integrates with back-end provers and supports interactive proof d
  name: TLAPS Proof System
  slug: tlaps-proof-system
- description: The TLA+ Toolbox is a full-featured IDE for writing TLA+ specifications, running TLC model checks, and managing proofs with TLAPS. Available as a standalone Eclipse-based application.
  name: TLA+ Toolbox IDE
  slug: tla-toolbox-ide
- description: The official TLA+ extension for Visual Studio Code providing language support, syntax highlighting, TLC integration, and model checking from within the VS Code editor.
  name: TLA+ VS Code Extension
  slug: vscode-tlaplus
- description: A curated collection of TLA+ snippets, operators, and modules contributed by the TLA+ community, providing reusable formal specification components for common patterns in concurrent and distributed sy
  name: TLA+ Community Modules
  slug: community-modules
- description: A collection of TLA+ specifications of varying complexity covering distributed algorithms, consensus protocols, concurrent data structures, and system models. Includes reference implementations for le
  name: TLA+ Specification Examples
  slug: tlaplus-examples
artifact_total: 30
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tlaplus/tlaplus/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/tlaplus/tlaplus/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/tlaplus/tlaplus/blob/master/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/tlaplus/tlaplus/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/tlaplus/tlaplus/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tla-plus-foundation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://foundation.tlapl.us/
- group: docs
  title: ''
  type: Documentation
  url: https://lamport.azurewebsites.net/tla/tla.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tlaplus
- group: operate
  title: ''
  type: Support
  url: mailto:support@tlapl.us
created: '2026-03-16'
description: The TLA+ Foundation is an independent nonprofit hosted by the Linux Foundation, dedicated to fostering the adoption of the TLA+ specification language in industry, academia, and education. Created by Leslie Lamport, TLA+ is a high-level formal specification language based on set theory and temporal logic for modeling concurrent and distributed systems. Inaugural members include Amazon Web Services (AWS) and Oracle. The Foundation funds research and development, maintains the TLC model checker, TLAPS proof system, and TLA+ Toolbox IDE, and coordinates community resources including the VS Code extension, CommunityModules, and formal verification examples. The current stable release is v1.7.4 (The Xenophanes release).
features:
- description: Explicit-state model checker for TLA+ specifications supporting both exhaustive verification and simulation modes.
  name: TLC Model Checker
- description: Interactive proof manager for formally verifying TLA+ specifications against mathematical proofs.
  name: TLAPS Proof System
- description: Eclipse-based IDE for writing, model-checking, and managing TLA+ specifications with TLAPS integration.
  name: TLA+ Toolbox IDE
- description: Official Visual Studio Code extension providing TLA+ language support and TLC integration.
  name: VS Code Extension
- description: Reusable TLA+ operator and module library contributed and maintained by the community.
  name: Community Modules
- description: Foundation grants funding research and industry initiatives to advance TLA+ specification and tool adoption.
  name: Grant Program
- description: TLA+ tools available as Maven Java dependency from central.sonatype.org for programmatic integration.
  name: Maven Package Distribution
- description: Python interpreter for executing TLA+ specifications, enabling Python-based formal modeling workflows.
  name: PlusPy Python Interpreter
finops:
- name: Tla Plus Foundation Finops
  service_category: API
  slug: tla-plus-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tla-plus-foundation.png
integrations:
- description: Founding member; AWS uses TLA+ for distributed systems design including DynamoDB and S3 protocols.
  name: Amazon Web Services
- description: Founding member; uses TLA+ for database and distributed system specification.
  name: Oracle
- description: Early TLA+ adopter for Azure and distributed systems formal verification.
  name: Microsoft
- description: Official VS Code extension for TLA+ editing and model checking.
  name: Visual Studio Code
- description: TLA+ tools distributed as Java Maven dependency for programmatic integration.
  name: Maven Central
- description: Parent organization hosting the TLA+ Foundation as an independent nonprofit project.
  name: Linux Foundation
layout: provider
modified: '2026-05-03'
name: TLA Plus Foundation
nav: Providers
network: true
overview: 'TLA Plus Foundation publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Formal Methods, Linux Foundation, Specifications, Verification, and Distributed Systems.


  TLA Plus Foundation''s developer surface includes documentation, support, and 8 more developer resources.'
plans:
- name: Tla Plus Foundation Plans Pricing
  plan_count: 3
  slug: tla-plus-foundation-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Tla Plus Foundation Rate Limits
  slug: tla-plus-foundation-rate-limits
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 20.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tla-plus-foundation/refs/heads/main/screenshots/tla-plus-foundation-2026-06-20T195420.png
security:
- kind: domain-security
  name: Tla Plus Foundation Domain Security
  slug: tla-plus-foundation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tla-plus-foundation
tags:
- Formal Methods
- Linux Foundation
- Specifications
- Verification
- Distributed Systems
- Concurrency
use_cases:
- description: Model-check distributed consensus, replication, and coordination protocols against safety and liveness properties.
  name: Distributed Algorithm Verification
- description: Formally specify concurrent data structures, lock-free algorithms, and parallel systems using TLA+.
  name: Concurrent System Specification
- description: Use TLA+ to design and validate network protocols, database transactions, and API contracts before implementation.
  name: Protocol Design and Validation
- description: Embed TLC model checking in CI/CD pipelines or custom tools using the tla2tools Maven dependency.
  name: Tooling Integration via Java API
- description: Use the TLA+ Toolbox, VS Code extension, and Leslie Lamport's video course to learn formal methods.
  name: Education and Training
- description: Use TLAPS to produce machine-checked proofs of safety and liveness properties for critical systems.
  name: Safety and Liveness Proof
website: https://foundation.tlapl.us/
---
