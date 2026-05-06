---
aid: chief-information-officers-council
name: Chief Information Officers Council
x-type: government
description: The Chief Information Officers Council (CIOC) is the principal interagency forum for improving agency practices related to the design, acquisition, development, modernization, use, sharing, and performance of federal information resources. Established by Executive Order 13011 in 1996 and codified in the E-Government Act of 2002 (44 U.S.C. 3603), the Council is comprised of the Chief Information Officers and Deputy CIOs of executive branch agencies, the Federal CIO at OMB (who serves as Chair), the Federal Chief Information Security Officer, and the Administrator for Electronic Government. The CIOC develops recommendations for OMB IT policy, identifies opportunities to improve federal IT performance, coordinates multi-agency IT initiatives such as cybersecurity and cloud adoption, supports federal IT workforce development, and disseminates effective IT management practices across the federal government. The Council publishes guidance, playbooks, and resources through cio.gov and councils.gov.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/chief-information-officers-council/refs/heads/main/apis.yml
tags:
  - CIO
  - Cloud
  - Cybersecurity
  - E-Government
  - Federal Government
  - IT Modernization
  - Information Technology
  - Interagency Council
  - OMB
  - Public Sector
created: '2024-12-03'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: chief-information-officers-council:cioc-resources
    name: Chief Information Officers Council Resources
    description: The CIOC publishes its charter, leadership roster, committee output, playbooks (e.g., Cloud Smart, Modular Contracting, IT Modernization), and federal IT guidance through cio.gov and councils.gov. The Council does not expose a dedicated developer API; resources are distributed as web pages, PDFs, and downloadable documents alongside OMB and GSA federal IT management resources.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.councils.gov/cioc
    tags:
      - Federal Government
      - Information Technology
    properties:
      - type: Documentation
        url: https://www.councils.gov/cioc
      - type: LegacyWebsite
        url: https://www.cio.gov
      - type: Statute
        url: https://www.law.cornell.edu/uscode/text/44/3603
common:
  - type: Website
    url: https://www.councils.gov/cioc
  - type: LegacyWebsite
    url: https://www.cio.gov
  - type: ParentAgency
    name: Office of Management and Budget (OMB)
    url: https://www.whitehouse.gov/omb/
  - type: Statute
    name: E-Government Act of 2002 (44 USC 3603)
    url: https://www.law.cornell.edu/uscode/text/44/3603
  - type: ExecutiveOrder
    name: Executive Order 13011 (1996)
    url: https://www.federalregister.gov/documents/1996/07/19/96-18638/federal-information-technology
  - type: FederalCIO
    url: https://www.whitehouse.gov/omb/management/ofcio/
  - type: GSAOfficeOfGovernmentwidePolicy
    url: https://www.gsa.gov/policy-regulations/policy/it-policy
  - type: FedRAMP
    url: https://www.fedramp.gov
  - type: TechnologyModernizationFund
    url: https://tmf.cio.gov
  - type: USAGov
    url: https://www.usa.gov/agencies/chief-information-officers-council
  - type: PrivacyPolicy
    url: https://www.councils.gov/privacy
  - name: Committees
    type: Committees
    data:
      - name: Innovation Committee
      - name: Workforce Committee
      - name: Information Security and Identity Management Committee (ISIMC)
      - name: Privacy Committee
      - name: Accessibility Committee
      - name: Shared Services Committee
      - name: Modernization and Migration Committee
  - name: Programs
    type: Programs
    data:
      - name: Federal CIO Office (OMB)
      - name: Federal Chief Information Security Officer Council
      - name: Federal Risk and Authorization Management Program (FedRAMP)
      - name: Technology Modernization Fund (TMF)
      - name: U.S. Digital Service
      - name: 18F (GSA)
      - name: National Initiative for Cybersecurity Education (NICE)
  - name: Features
    type: Features
    data:
      - name: Senior-Level Interagency Forum
      - name: Federal IT Policy Coordination
      - name: Cybersecurity Standards and Guidance
      - name: IT Modernization Playbooks
      - name: Cloud Adoption (Cloud Smart)
      - name: Federal IT Workforce Development
      - name: Federal Identity, Credential, and Access Management (FICAM)
      - name: Open Government and Data Sharing
  - name: UseCases
    type: UseCases
    data:
      - name: Federal IT Modernization
      - name: Cloud Migration and Adoption
      - name: Cybersecurity Posture Improvement
      - name: Federal IT Workforce Development
      - name: Cross-Agency IT Best Practice Sharing
      - name: FedRAMP Authorization Coordination
      - name: Identity, Credential, and Access Management
      - name: Federal Data Strategy Implementation
  - name: Standards
    type: Standards
    data:
      - name: E-Government Act of 2002 (44 USC 3603)
      - name: Federal Information Security Modernization Act (FISMA)
      - name: NIST Cybersecurity Framework
      - name: NIST SP 800-53 (Security and Privacy Controls)
      - name: Federal Information Processing Standards (FIPS)
      - name: OMB Circular A-130 (Managing Information as a Strategic Resource)
      - name: Cloud Smart Strategy
      - name: Federal Data Strategy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
