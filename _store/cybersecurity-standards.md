---
aid: cybersecurity-standards
name: Cybersecurity Standards
x-type: topic
description: Cybersecurity Standards captures the public, machine-readable, and reference frameworks that establish best practices for protecting information systems, networks, software, and data from cyber threats. The landscape is anchored by U.S. National Institute of Standards and Technology (NIST) publications such as the Cybersecurity Framework (CSF) 2.0, SP 800-53 controls, SP 800-171 controls for controlled unclassified information, the Risk Management Framework (RMF), and the Secure Software Development Framework (SSDF SP 800-218); the international ISO/IEC 27001 / 27002 information security management standard family; the Center for Internet Security (CIS) Critical Security Controls and Benchmarks; the OWASP Top 10 and ASVS for application security; PCI DSS for payment data; HITRUST CSF for healthcare; SOC 2 trust services criteria; and FedRAMP / StateRAMP for cloud authorization. This index aggregates authoritative URLs, machine-readable artifacts (e.g., OSCAL), and cross-references for organizations building or auditing cybersecurity programs.
url: https://raw.githubusercontent.com/api-evangelist/cybersecurity-standards/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Reference
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - CIS Controls
  - Compliance
  - CSF
  - Cybersecurity
  - FedRAMP
  - Frameworks
  - HIPAA
  - HITRUST
  - Information Security
  - ISO 27001
  - ISO 27002
  - NIST
  - NIST 800-171
  - NIST 800-218
  - NIST 800-53
  - OSCAL
  - OWASP
  - PCI DSS
  - Risk Management
  - SOC 2
  - SSDF
  - Standards
apis:
  - aid: cybersecurity-standards:nist-csf
    name: NIST Cybersecurity Framework (CSF) 2.0
    description: The NIST Cybersecurity Framework 2.0 is a voluntary risk-based framework organizing cybersecurity activities into six core functions (Govern, Identify, Protect, Detect, Respond, Recover) with categories and subcategories. NIST publishes informative references and quick-start guides mapping CSF to other standards.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.nist.gov/cyberframework
    tags:
      - CSF
      - Framework
      - NIST
      - Risk Management
    properties:
      - type: Documentation
        url: https://www.nist.gov/cyberframework
      - type: Publication
        url: https://doi.org/10.6028/NIST.CSWP.29
      - type: QuickStartGuides
        url: https://www.nist.gov/cyberframework/quick-start-guides
      - type: InformativeReferences
        url: https://www.nist.gov/cyberframework/informative-references
  - aid: cybersecurity-standards:nist-800-53
    name: NIST SP 800-53 Security and Privacy Controls
    description: NIST Special Publication 800-53 Revision 5 catalogs security and privacy controls for information systems and organizations. Used as the basis of FedRAMP authorizations and Risk Management Framework implementations. Available in machine-readable OSCAL format.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
    tags:
      - Controls
      - FedRAMP
      - NIST
      - OSCAL
      - RMF
    properties:
      - type: Documentation
        url: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
      - type: OSCALContent
        url: https://github.com/usnistgov/oscal-content
      - type: ControlBaselines
        url: https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search
  - aid: cybersecurity-standards:nist-800-171
    name: NIST SP 800-171 Protecting CUI
    description: NIST SP 800-171 specifies requirements for protecting Controlled Unclassified Information (CUI) in non-federal systems. Forms the basis of CMMC (Cybersecurity Maturity Model Certification) for the U.S. defense industrial base.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
    tags:
      - CMMC
      - CUI
      - DIB
      - NIST
    properties:
      - type: Documentation
        url: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
      - type: Assessment
        url: https://csrc.nist.gov/publications/detail/sp/800-171a/rev-3/final
  - aid: cybersecurity-standards:nist-ssdf
    name: NIST SP 800-218 Secure Software Development Framework (SSDF)
    description: NIST SP 800-218 defines the Secure Software Development Framework (SSDF), a set of high-level secure-development practices referenced by U.S. Executive Order 14028 and procurement attestations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://csrc.nist.gov/publications/detail/sp/800-218/final
    tags:
      - NIST
      - Secure Development
      - SSDF
    properties:
      - type: Documentation
        url: https://csrc.nist.gov/publications/detail/sp/800-218/final
  - aid: cybersecurity-standards:iso-27001
    name: ISO/IEC 27001 Information Security Management
    description: ISO/IEC 27001 is the international standard for information security management systems (ISMS). The 2022 revision aligns Annex A controls with the ISO/IEC 27002:2022 catalog. Certification is performed by accredited bodies.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.iso.org/standard/27001
    tags:
      - Certification
      - ISMS
      - ISO 27001
      - ISO 27002
    properties:
      - type: Documentation
        url: https://www.iso.org/standard/27001
      - type: ISO27002
        url: https://www.iso.org/standard/75652.html
  - aid: cybersecurity-standards:cis-controls
    name: CIS Critical Security Controls and Benchmarks
    description: The Center for Internet Security publishes the Critical Security Controls (currently v8.1) and a library of CIS Benchmarks providing prescriptive secure configuration guidance for OSes, cloud platforms, and applications.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cisecurity.org/controls
    tags:
      - Benchmarks
      - CIS
      - Configuration
      - Controls
    properties:
      - type: Documentation
        url: https://www.cisecurity.org/controls
      - type: Benchmarks
        url: https://www.cisecurity.org/cis-benchmarks
  - aid: cybersecurity-standards:owasp
    name: OWASP Top 10 and ASVS
    description: OWASP publishes the Top 10 web application risks, the API Security Top 10, and the Application Security Verification Standard (ASVS) used as a baseline for application security reviews.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://owasp.org/Top10/
    tags:
      - API Security
      - ASVS
      - AppSec
      - OWASP
    properties:
      - type: Top10
        url: https://owasp.org/Top10/
      - type: APITop10
        url: https://owasp.org/API-Security/
      - type: ASVS
        url: https://owasp.org/www-project-application-security-verification-standard/
  - aid: cybersecurity-standards:pci-dss
    name: PCI DSS Payment Card Industry Data Security Standard
    description: PCI DSS, maintained by the PCI Security Standards Council, defines requirements for organizations that store, process, or transmit cardholder data. Version 4.0.1 is the current edition.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.pcisecuritystandards.org/
    tags:
      - Cardholder Data
      - Payments
      - PCI DSS
    properties:
      - type: Documentation
        url: https://www.pcisecuritystandards.org/document_library/
  - aid: cybersecurity-standards:soc2
    name: SOC 2 Trust Services Criteria
    description: SOC 2 (System and Organization Controls 2) reports are issued by AICPA-licensed auditors against the Trust Services Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy). Widely adopted by SaaS vendors.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2
    tags:
      - AICPA
      - Audit
      - SOC 2
      - Trust Services
    properties:
      - type: Documentation
        url: https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2
  - aid: cybersecurity-standards:fedramp
    name: FedRAMP Federal Cloud Authorization
    description: The Federal Risk and Authorization Management Program provides a standardized approach for U.S. federal agencies to authorize cloud services, anchored on NIST SP 800-53 baselines.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.fedramp.gov/
    tags:
      - Cloud
      - FedRAMP
      - Federal Government
    properties:
      - type: Documentation
        url: https://www.fedramp.gov/
      - type: Marketplace
        url: https://marketplace.fedramp.gov/
common:
  - type: NIST
    url: https://www.nist.gov/cyberframework
  - type: NISTCSRC
    url: https://csrc.nist.gov/
  - type: OSCALContent
    url: https://github.com/usnistgov/oscal-content
  - type: ISO
    url: https://www.iso.org/standard/27001
  - type: CIS
    url: https://www.cisecurity.org/
  - type: OWASP
    url: https://owasp.org/
  - type: PCI
    url: https://www.pcisecuritystandards.org/
  - type: AICPA
    url: https://www.aicpa-cima.com/
  - type: FedRAMP
    url: https://www.fedramp.gov/
  - type: HITRUST
    url: https://hitrustalliance.net/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
