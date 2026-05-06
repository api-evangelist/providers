---
aid: code-of-conduct-md
url: https://raw.githubusercontent.com/api-evangelist/code-of-conduct-md/refs/heads/main/apis.yml
name: CODE_OF_CONDUCT.md
tags:
  - Community
  - Contributor Covenant
  - Governance
  - Open Source
  - Repository File
  - Standards
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: standard
created: '2025-01-01'
modified: '2026-04-26'
position: Consumer
description: CODE_OF_CONDUCT.md is the de-facto repository file used by open-source projects on GitHub, GitLab, and similar platforms to declare community standards, acceptable behavior, and enforcement procedures for project participants. The most widely adopted text dropped into this file is the Contributor Covenant, currently at version 2.1, maintained by the Organization for Ethical Source. GitHub surfaces a CODE_OF_CONDUCT.md located in the repo root, .github/, or docs/ directory in its Community Standards checklist and links to it from issue templates. The file is plain Markdown and has no machine-readable schema, but it is structurally consistent across the dominant template (Contributor Covenant) and a small number of alternatives (Citizen Code of Conduct, Django Code of Conduct, Mozilla Community Participation Guidelines).
x-status: De facto convention
x-canonical-template: Contributor Covenant 2.1
x-current-version: '2.1'
x-licenses:
  - name: Contributor Covenant
    license: CC BY 4.0
    url: https://www.contributor-covenant.org/
x-discovery:
  - GitHub displays community profile entry when CODE_OF_CONDUCT.md exists
  - Looks for the file in /, .github/, or docs/ (first found wins)
  - GitHub also offers a Code of Conduct picker via Insights -> Community
x-typical-sections:
  - Our Pledge
  - Our Standards
  - Enforcement Responsibilities
  - Scope
  - Enforcement (contact and reporting)
  - Enforcement Guidelines / Community Impact Ladder
  - Attribution
x-enforcement-ladder:
  - level: Correction
    impact: Use of inappropriate language or unprofessional behavior
    consequence: Private written warning with explanation; public apology may be requested
  - level: Warning
    impact: A violation through a single incident or series of actions
    consequence: Warning with consequences for continued behavior; no interaction with the parties involved for a specified period
  - level: Temporary Ban
    impact: A serious violation of community standards
    consequence: Temporary ban from any public interaction or communication with the community
  - level: Permanent Ban
    impact: Demonstrating a pattern of violation, harassment, or aggression
    consequence: Permanent ban from any public interaction within the community
x-related-files:
  - CONTRIBUTING.md
  - SECURITY.md
  - GOVERNANCE.md
  - SUPPORT.md
  - CODEOWNERS
  - LICENSE
apis: []
common:
  - type: Specification
    url: https://www.contributor-covenant.org/version/2/1/code_of_conduct/
  - type: Reference
    url: https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md
  - type: Website
    url: https://www.contributor-covenant.org/
  - type: Translations
    url: https://www.contributor-covenant.org/translations/
  - type: Documentation
    url: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project
  - type: Documentation
    url: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-management-and-moderation
  - type: AlternateStandard
    url: https://citizencodeofconduct.org/
  - type: AlternateStandard
    url: https://www.djangoproject.com/conduct/
  - type: AlternateStandard
    url: https://www.mozilla.org/en-US/about/governance/policies/participation/
  - type: License
    url: https://creativecommons.org/licenses/by/4.0/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
