---
aid: administrative-conference-of-the-united-states
url: https://raw.githubusercontent.com/api-evangelist/administrative-conference-of-the-united-states/refs/heads/main/apis.yml
name: Administrative Conference of the United States
created: '2024-11-20'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Federal Government
  - Regulatory Reform
  - Administrative Law
  - Government Efficiency
  - Open Data
  - Policy Research
description: The Administrative Conference of the United States (ACUS) is an independent federal agency within the executive branch whose statutory mission is to identify ways to improve the procedures by which federal agencies administer regulatory, benefit, and other government programs. ACUS issues approximately a dozen recommendations per year to agencies, Congress, the President, and the Judicial Conference, aimed at enhancing efficiency and fairness in administrative procedures. The agency maintains the Federal Administrative Adjudication Database (with Stanford Law School), the Equal Access to Justice Act (EAJA) online database, and various open data resources under the Foundations for Evidence-Based Policymaking Act of 2018.
apis:
  - aid: administrative-conference-of-the-united-states:eaja-database
    name: Equal Access to Justice Act (EAJA) Database
    description: ACUS maintains an online database of Equal Access to Justice Act (EAJA) awards, tracking awards of attorney's fees and other costs against the United States government. ACUS collects and reports this information to Congress annually, with data accessible through the ACUS website. The database provides transparency into government litigation costs and EAJA awards by agency, fiscal year, and case type.
    humanURL: https://www.acus.gov/data
    tags:
      - Equal Access to Justice
      - Administrative Law
      - Open Data
      - Legal
    properties:
      - type: Documentation
        url: https://www.acus.gov/data
      - type: DataAPI
        url: https://www.acus.gov/data
  - aid: administrative-conference-of-the-united-states:federal-administrative-adjudication-database
    name: Federal Administrative Adjudication Database
    description: A joint project between ACUS and Stanford Law School, the Federal Administrative Adjudication Database provides comprehensive data on federal agency adjudication processes across the U.S. government. The database tracks administrative law judges, adjudicative proceedings, hearing processes, and adjudication statistics across federal agencies to support research and policy reform.
    humanURL: https://acus.gov/recommendations
    tags:
      - Administrative Law
      - Adjudication
      - Open Data
      - Research
    properties:
      - type: Documentation
        url: https://acus.gov/recommendations
      - type: DataAPI
        url: https://acus.gov/recommendations
common:
  - type: Website
    url: https://www.acus.gov/
  - type: Portal
    url: https://www.acus.gov/
  - type: Resources
    url: https://www.acus.gov/page/resources
  - type: Contact
    url: https://www.acus.gov/about-acus
  - type: Features
    data:
      - name: Regulatory Reform Recommendations
        description: Issues approximately a dozen formal recommendations per year to federal agencies, Congress, the President, and the Judicial Conference aimed at improving the efficiency, fairness, and transparency of administrative procedures and regulatory programs.
      - name: Federal Administrative Adjudication Database
        description: Joint project with Stanford Law School providing comprehensive data on federal agency adjudication processes, administrative law judges, and hearing statistics across all federal agencies.
      - name: Equal Access To Justice Act (EAJA) Reporting
        description: Annual reporting to Congress on awards of attorney's fees and costs against the United States under EAJA, with an online database of all EAJA awards accessible to the public.
      - name: Sourcebook Of US Executive Agencies
        description: Comprehensive reference resource documenting the structure, authority, and programs of all U.S. executive agencies, updated periodically to reflect organizational changes.
      - name: Administrative Law Research And Publications
        description: ACUS consultants and staff prepare research reports, model rules, and periodic summaries of administrative law reform bills on topics related to administrative procedure and government efficiency.
      - name: Open Government Data Initiative
        description: ACUS maintains open data resources and has designated a Chief Data Officer in compliance with the Foundations for Evidence-Based Policymaking Act of 2018.
  - type: UseCases
    data:
      - name: Administrative Law Research
        description: Legal researchers, law schools, and practitioners can access ACUS recommendations, reports, and the adjudication database to study trends in federal administrative law and regulatory practice.
      - name: Regulatory Process Benchmarking
        description: Federal agencies can use ACUS recommendations and research to benchmark their regulatory and adjudicative procedures against best practices and ACUS-recommended reforms.
      - name: EAJA Litigation Cost Analysis
        description: Researchers and policymakers can use the EAJA database to analyze government litigation costs, identify agencies with high fee award rates, and evaluate the effectiveness of EAJA in providing access to justice.
      - name: Rulemaking Process Reform
        description: Congressional staff and agency officials can draw on ACUS reports and model rules for guidance on improving rulemaking procedures, notice-and-comment processes, and public participation.
      - name: Government Efficiency Analysis
        description: Public interest organizations and policy researchers can use ACUS data and publications to analyze opportunities for improving government administrative processes and reducing regulatory burdens.
maintainers:
  - FN: Kin Lane
    X-twitter: apievangelist
    email: info@apievangelist.com
---
