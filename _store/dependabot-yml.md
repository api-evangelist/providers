---
aid: dependabot-yml
name: Dependabot.yml
description: GitHub Dependabot configuration file defining automated dependency update schedules, package ecosystems to monitor, grouping, cooldown, and review assignment rules.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - CI/CD
  - Dependency Management
  - GitHub
  - Security
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: dependabot-yml:dependabot-config
    name: Dependabot Configuration
    description: The dependabot.yml schema, examples, validation rules, and capability catalog for configuring GitHub Dependabot.
    tags:
      - Configuration
      - YAML
      - Dependabot
    properties:
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/main/json-schema/dependabot-config-schema.json
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/main/rules/dependabot-config-rules.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/main/capabilities/dependabot-yml-capabilities.md
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/main/examples/basic-npm.yml
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/main/examples/multi-ecosystem.yml
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/main/examples/grouped-security.yml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/main/vocabulary/dependabot-yml-vocabulary.json
      - type: JSON-LD
        url: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/main/json-ld/dependabot-yml.jsonld
common:
  - type: Documentation
    url: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file
  - type: GitHub Organization
    url: https://github.com/api-evangelist
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
