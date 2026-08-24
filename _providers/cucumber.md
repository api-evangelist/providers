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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 5
apis:
- description: Java/JVM implementation of Cucumber supporting Java, Kotlin, Scala, and other JVM languages. Distributed via Maven Central under the io.cucumber group.
  name: Cucumber JVM
  slug: cucumber-jvm
- description: JavaScript/Node.js implementation of Cucumber for running BDD tests in Node and the browser. Distributed as @cucumber/cucumber on npm.
  name: Cucumber.js
  slug: cucumber-js
- description: Ruby implementation of Cucumber, the original Cucumber project. Distributed as the cucumber gem on RubyGems.
  name: Cucumber Ruby
  slug: cucumber-ruby
- description: Gherkin is the language used to write Cucumber feature files. Parsers are published per language and emit Cucumber Messages that downstream tools consume.
  name: Gherkin
  slug: gherkin
- description: Protocol-buffer / JSON Schema specification of the messages exchanged between Cucumber components (parsers, runners, formatters). Implemented across all language ports for consistent reporting.
  name: Cucumber Messages
  slug: cucumber-messages
artifact_total: 12
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cucumber/cucumber-jvm/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cucumber/cucumber-jvm/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cucumber/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cucumber/cucumber-jvm/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/cucumber/cucumber-jvm/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cucumber-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cucumber.io
- group: docs
  title: ''
  type: Documentation
  url: https://cucumber.io/docs
- group: docs
  title: ''
  type: Reference
  url: https://cucumber.io/docs/gherkin/reference/
- group: other
  title: ''
  type: School
  url: https://school.cucumber.io
- group: build
  title: ''
  type: Tools
  url: https://cucumber.io/tools
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cucumber
- group: other
  title: ''
  type: X
  url: https://twitter.com/cucumberbdd
- group: operate
  title: ''
  type: Slack
  url: https://cucumber.io/community#slack
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCVhQ7ulinkFAkUx3eNvzoEg
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cucumber-message-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cucumber-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cucumber-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://cucumber.io/blog/atom.xml
created: '2024-01-01'
description: Cucumber is an open-source Behavior Driven Development (BDD) tool for running automated tests written in plain language using the Gherkin syntax. It enables collaboration between technical and non-technical team members by expressing executable specifications as Given/When/Then scenarios. Cucumber has implementations for many languages (JVM, JavaScript, Ruby, .NET, Python, Go, Rust) and a shared message protocol that connects parsers, runners, and reporters.
finops:
- name: Cucumber Finops
  service_category: API
  slug: cucumber-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cucumber.png
json_schemas:
- name: CucumberMessage
  property_count: 11
  slug: cucumber-message
jsonld:
- class_count: 23
  name: Cucumber Context
  property_count: 2
  slug: cucumber-context
layout: provider
modified: '2026-04-28'
name: Cucumber
nav: Providers
network: true
overview: 'Cucumber publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, BDD, Behavior-Driven Development, Gherkin, and Open-Source.


  The Cucumber catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cucumber''s developer surface includes documentation, tooling, YouTube channel, engineering blog, and 15 more developer resources.'
plans:
- name: Cucumber Plans Pricing
  plan_count: 3
  slug: cucumber-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Cucumber Rate Limits
  slug: cucumber-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cucumber API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cucumber-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.7
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 19.7
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 25.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cucumber/refs/heads/main/screenshots/cucumber-2026-06-20T175327.png
security:
- kind: domain-security
  name: Cucumber Domain Security
  slug: cucumber-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cucumber
tags:
- Automation
- BDD
- Behavior-Driven Development
- Gherkin
- Open-Source
- Quality Assurance
- Test Framework
- Testing
website: https://cucumber.io
---
