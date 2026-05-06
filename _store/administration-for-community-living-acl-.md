---
aid: administration-for-community-living-acl-
url: https://raw.githubusercontent.com/api-evangelist/administration-for-community-living-acl-/refs/heads/main/apis.yml
name: Administration for Community Living (ACL)
created: '2024-11-20'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Aging
  - Federal Government
  - Healthcare
  - Disability
  - Independent Living
  - Open Data
  - Social Services
description: The Administration for Community Living (ACL) is part of the United States Department of Health and Human Services. ACL works to maximize the independence, well-being, and health of older adults, people with disabilities across the lifespan, and their families and caregivers. The agency administers the Older Americans Act programs, supports disability services through centers for independent living, and maintains the AGing, Independence, and Disability (AGID) Program Data Portal providing publicly accessible datasets on aging and disability programs. ACL also operates the National Institute on Disability, Independent Living and Rehabilitation Research (NIDILRR).
apis:
  - aid: administration-for-community-living-acl-:agid-data-portal
    name: AGID Program Data Portal
    description: The AGing, Independence, and Disability (AGID) Program Data Portal provides publicly accessible data from programs funded under the Older Americans Act and related disability programs. Datasets include the American Community Survey Special Tabulation on Aging and Disability, National Survey of Older Americans Act Participants (NSOAAP), National Ombudsman Reporting System (NORS), National Adult Maltreatment Reporting System (NAMRS), Independent Living Services (ILS) and Centers for Independent Living (CIL) performance data, and I/DD (Intellectual and Developmental Disabilities) Longitudinal Data. Data files are available for download in CSV and Excel formats.
    humanURL: https://agid.acl.gov/
    tags:
      - Aging
      - Disability
      - Open Data
      - Older Americans Act
      - Independent Living
    properties:
      - type: Documentation
        url: https://agid.acl.gov/
      - type: DataAPI
        url: https://agid.acl.gov/DataFiles/
common:
  - type: Website
    url: https://acl.gov/
  - type: Portal
    url: https://agid.acl.gov/
  - type: DataAPI
    url: https://agid.acl.gov/DataFiles/
  - type: Resources
    url: https://acl.gov/aging-and-disability-in-america/data-and-research
  - type: Contact
    url: https://acl.gov/about-acl/contact-us
  - type: Features
    data:
      - name: Older Americans Act Program Data
        description: Data from programs funded under the Older Americans Act including nutrition services, caregiver support, elder rights, and home and community-based supportive services.
      - name: National Ombudsman Reporting System (NORS)
        description: Annual data from the Long-Term Care Ombudsman Program, covering complaints, facilities visited, and resident outcomes in nursing homes and assisted living facilities.
      - name: National Adult Maltreatment Reporting System (NAMRS)
        description: Standardized data from state Adult Protective Services programs on reports of abuse, neglect, and exploitation of adults.
      - name: Independent Living Program Data
        description: Annual performance data from states and territories administering Independent Living Services and Centers for Independent Living (CIL) programs under the Rehabilitation Act.
      - name: I/DD Longitudinal Data
        description: 'Longitudinal data tracking intellectual and developmental disability services across three areas: revenue and spending, residential supports, and employment services.'
      - name: American Community Survey Disability Data
        description: Special tabulations from the U.S. Census Bureau American Community Survey providing demographic and household data for older adults and people with disabilities.
      - name: FOIA Request Services
        description: Freedom of Information Act (FOIA) services enabling public access to ACL agency records not otherwise publicly available.
  - type: UseCases
    data:
      - name: Aging Services Research And Planning
        description: Researchers and state agencies can access AGID data to analyze trends in aging services utilization, outcomes, and demographics to inform program planning.
      - name: Long-Term Care Ombudsman Analysis
        description: Policy researchers can use NORS data to analyze complaint trends, facility quality indicators, and resident outcomes in long-term care settings.
      - name: Adult Protective Services Benchmarking
        description: State APS programs and advocates can use NAMRS data to benchmark reporting, investigation, and service delivery across states.
      - name: Disability Employment And Housing Research
        description: Researchers can analyze I/DD longitudinal data to track trends in employment, residential services, and community integration for people with intellectual and developmental disabilities.
      - name: Community Living Policy Development
        description: Federal and state policymakers can use ACL data to evaluate the impact of community living initiatives and identify gaps in service delivery.
maintainers:
  - FN: Kin Lane
    X-twitter: apievangelist
    email: info@apievangelist.com
---
