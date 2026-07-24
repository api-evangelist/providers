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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apache Software Foundation Agentic Access
  operation_count: 14
  slug: apache-software-foundation-agentic-access
  summary_line: 14 operations
api_count: 9
apis:
- description: The Apache Software Foundation Projects API provides read-only access to JSON data about ASF projects, committees, releases, and podlings. The data is served as static JSON files from projects.apache.
  name: Apache Software Foundation Projects API
  slug: projects-api
- description: The Committees API from Apache Software Foundation — 3 operation(s) for committees.
  name: Apache Software Foundation Committees API
  slug: apache-software-foundation-committees-api
- description: The Foundation API from Apache Software Foundation — 1 operation(s) for foundation.
  name: Apache Software Foundation Foundation API
  slug: apache-software-foundation-foundation-api
- description: The Groups API from Apache Software Foundation — 1 operation(s) for groups.
  name: Apache Software Foundation Groups API
  slug: apache-software-foundation-groups-api
- description: The ICLA API from Apache Software Foundation — 1 operation(s) for icla.
  name: Apache Software Foundation ICLA API
  slug: apache-software-foundation-icla-api
- description: The Members API from Apache Software Foundation — 1 operation(s) for members.
  name: Apache Software Foundation Members API
  slug: apache-software-foundation-members-api
- description: The People API from Apache Software Foundation — 3 operation(s) for people.
  name: Apache Software Foundation People API
  slug: apache-software-foundation-people-api
- description: The Podlings API from Apache Software Foundation — 2 operation(s) for podlings.
  name: Apache Software Foundation Podlings API
  slug: apache-software-foundation-podlings-api
- description: The Releases API from Apache Software Foundation — 1 operation(s) for releases.
  name: Apache Software Foundation Releases API
  slug: apache-software-foundation-releases-api
artifact_total: 41
collections:
- collection_type: open
  name: Apache Software Foundation Projects API
  slug: open-apache-software-foundation-projects-api
- collection_type: open
  name: Apache Software Foundation Whimsy Public Data API
  slug: open-apache-software-foundation-whimsy-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-software-foundation-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-software-foundation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-software-foundation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-apache-software-foundation
- group: start
  title: ''
  type: Portal
  url: https://www.apache.org/
- group: company
  title: ''
  type: Blog
  url: https://blogs.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.apache.org/foundation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-software-foundation-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-software-foundation-vocabulary.yaml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
created: '2025-01-01'
description: APIs for the Apache Software Foundation (ASF), a nonprofit organization that supports the development of open-source software projects under the Apache License, providing governance, legal protection, and infrastructure for over 350 projects. The ASF exposes public APIs for project discovery, committee governance data, member information, and organizational structure through its Projects API and Whimsy Public Data API.
examples:
- key_count: 9
  name: Apache Software Foundation Committee Example
  slug: apache-software-foundation-committee-example
- key_count: 10
  name: Apache Software Foundation Podling Example
  slug: apache-software-foundation-podling-example
- key_count: 12
  name: Apache Software Foundation Project Example
  slug: apache-software-foundation-project-example
features:
- description: Comprehensive directory of all 350+ ASF top-level projects with metadata.
  name: Project Directory
- description: Project Management Committee membership, chair, and governance information.
  name: Committee Data
- description: Apache Incubator podling status, mentors, and graduation tracking.
  name: Podling Tracking
- description: Release version and date history for all ASF projects.
  name: Release History
- description: Public member, committer, and ICLA data from the ASF Whimsy system.
  name: Whimsy Member Data
finops:
- name: Apache Software Foundation Finops
  service_category: API
  slug: apache-software-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-software-foundation.png
integrations:
- description: All ASF project repositories hosted under the apache GitHub organization.
  name: Apache GitHub Organization
- description: Issue tracking at issues.apache.org for all ASF project bug reports and features.
  name: ASF JIRA
- description: Wiki documentation at cwiki.apache.org for ASF project and foundation docs.
  name: Apache Confluence
json_schemas:
- name: Apache Software Foundation Committee
  property_count: 9
  slug: apache-software-foundation-committee
- name: Apache Software Foundation Podling
  property_count: 10
  slug: apache-software-foundation-podling
- name: Apache Software Foundation Project
  property_count: 12
  slug: apache-software-foundation-project
json_structures:
- name: Apache Software Foundation Committee Structure
  property_count: 9
  slug: apache-software-foundation-committee-structure
- name: Apache Software Foundation Podling Structure
  property_count: 10
  slug: apache-software-foundation-podling-structure
- name: Apache Software Foundation Project Structure
  property_count: 12
  slug: apache-software-foundation-project-structure
jsonld:
- class_count: 5
  name: Apache Software Foundation Asf Context
  property_count: 22
  slug: apache-software-foundation-asf-context
layout: provider
modified: '2026-05-19'
name: Apache Software Foundation
nav: Providers
network: true
overview: 'Apache Software Foundation publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Projects API, Committees API, Foundation API, and 6 more. Tagged areas include ASF, Open Source, Governance, Projects, and Apache.


  The Apache Software Foundation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Software Foundation''s developer surface includes developer portal, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Apache Software Foundation Plans Pricing
  plan_count: 3
  slug: apache-software-foundation-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Apache Software Foundation Rate Limits
  slug: apache-software-foundation-rate-limits
rules:
- name: Apache Software Foundation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-software-foundation-jsonschema-spectral-rules
- name: Apache Software Foundation API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 11
  slug: apache-software-foundation-spectral-rules
score:
  band: developing
  composite: 51.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.7
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 51.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-software-foundation/refs/heads/main/screenshots/apache-software-foundation-2026-06-20T172144.png
security:
- kind: domain-security
  name: Apache Software Foundation Domain Security
  slug: apache-software-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Software Foundation Vulnerability Disclosure
  slug: apache-software-foundation-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-software-foundation
tags:
- ASF
- Open Source
- Governance
- Projects
- Apache
use_cases:
- description: Discover and explore all Apache Software Foundation projects programmatically.
  name: Apache Project Discovery
- description: Access committee membership and governance data for ASF organizational research.
  name: Governance Transparency
- description: Track release histories and versions across all ASF projects.
  name: Release Monitoring
- description: Monitor Apache Incubator podlings and their progression to top-level projects.
  name: Incubator Tracking
website: https://www.apache.org/
---
