---
aid: triple-s-management
name: Triple-S Management
url: https://raw.githubusercontent.com/api-evangelist/triple-s-management/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
description: Triple-S Management Corporation is the largest managed care company in Puerto Rico in terms of membership, providing health, life, and property and casualty insurance. A subsidiary of GuideWell (parent of Florida Blue), Triple-S operates as an independent licensee of the Blue Cross Blue Shield Association for Puerto Rico and the U.S. Virgin Islands. Its subsidiaries include Triple-S Salud (managed care), Triple-S Advantage (Medicare Advantage), Triple-S Vida (life insurance), Triple-S Propiedad (property and casualty), Salus (medical clinics), and CarePoint (IPA).
tags:
  - Health Insurance
  - Managed Care
  - Medicare Advantage
  - Puerto Rico
  - Blue Cross Blue Shield
  - Healthcare
apis:
  - aid: triple-s-management:triple-s-salud-provider-portal
    name: Triple-S Salud Provider Portal
    description: Mi Triple-S is the online provider portal for Triple-S Salud, offering healthcare providers access to insured eligibility verification, claims and payments management, re-credentialing, and provider directory. Supports electronic claims submission via EDI 837 transactions.
    humanURL: https://service.ssspr.com/provider/login.aspx
    baseURL: https://service.ssspr.com
    tags:
      - Provider Portal
      - Healthcare
      - Claims
      - Eligibility
      - EDI
    properties:
      - type: Provider Portal
        url: https://service.ssspr.com/provider/login.aspx
      - type: Documentation
        url: https://salud.grupotriples.com/en/providers/
  - aid: triple-s-management:triple-s-advantage-provider-portal
    name: Triple-S Advantage Provider Information
    description: Provider resources for Triple-S Advantage, the Medicare Advantage plan operated by Triple-S in Puerto Rico, including eligibility, prior authorizations, and claims management tools.
    humanURL: https://advantage.grupotriples.com/en/providers/
    baseURL: https://advantage.grupotriples.com
    tags:
      - Medicare Advantage
      - Provider Portal
      - Healthcare
    properties:
      - type: Documentation
        url: https://advantage.grupotriples.com/en/providers/
common:
  - type: Website
    url: https://www.triple-s-management.com
  - type: Corporate Website
    url: https://management.grupotriples.com/en/
  - type: Triple-S Salud
    url: https://salud.grupotriples.com/en/
  - type: Triple-S Advantage
    url: https://advantage.grupotriples.com/en/
  - type: Triple-S Vida
    url: https://vida.grupotriples.com/en/
  - type: Provider Portal
    url: https://service.ssspr.com/provider/login.aspx
  - type: Credentialing Platform
    url: https://www.ocshc.com/
  - type: Payment Portal
    url: https://ts.assertus.com/auth/login/index/
  - type: Member Portal
    url: https://salud.grupotriples.com/en/
  - type: Vocabulary
    url: vocabulary/triple-s-management-vocabulary.yml
  - type: JSON-LD
    url: json-ld/triple-s-management-context.jsonld
  - type: x-profiled
    url: 2026-05
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
