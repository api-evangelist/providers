---
aid: us-court-of-appeals-for-the-federal-circuit
url: https://raw.githubusercontent.com/api-evangelist/us-court-of-appeals-for-the-federal-circuit/refs/heads/main/apis.yml
apis:
  - aid: us-court-of-appeals-for-the-federal-circuit:pacer
    name: PACER - Public Access to Court Electronic Records
    tags:
      - Federal Courts
      - PACER
      - Case Records
      - Legal
    humanURL: https://pacer.uscourts.gov/file-case/court-cmecf-lookup/court/CAFC
    properties:
      - url: https://pacer.uscourts.gov/file-case/court-cmecf-lookup/court/CAFC
        type: Documentation
      - url: https://pacer.uscourts.gov/file-case/developer-resources
        type: APIReference
        title: PACER Developer Resources
      - url: https://pacer.uscourts.gov/help/pacer/pacer-authentication-api-user-guide
        type: Documentation
        title: PACER Authentication API User Guide
      - url: https://pacer.uscourts.gov/help/pacer/pacer-case-locator-pcl-api-user-guide
        type: Documentation
        title: PACER Case Locator (PCL) API User Guide
    description: Public Access to Court Electronic Records (PACER) provides online access to U.S. Federal Court case and docket information from Federal Courts including the U.S. Court of Appeals for the Federal Circuit (CAFC). PACER provides the Authentication API and the Case Locator (PCL) API for programmatic access to federal court records and case data.
  - aid: us-court-of-appeals-for-the-federal-circuit:opinions-orders
    name: Federal Circuit Opinions and Orders
    tags:
      - Federal Courts
      - Opinions
      - Legal Decisions
      - Legal
    humanURL: https://www.cafc.uscourts.gov/home/case-information/opinions-orders/
    properties:
      - url: https://www.cafc.uscourts.gov/home/case-information/opinions-orders/
        type: Documentation
        title: Opinions and Orders Search
    description: Public access to U.S. Court of Appeals for the Federal Circuit opinions, orders, and judgments. Includes precedential opinions, Rule 36 judgments, non-ministerial orders, and errata. Available online from October 1, 2004, to present. PDF documents accessible directly from cafc.uscourts.gov.
  - aid: us-court-of-appeals-for-the-federal-circuit:case-records
    name: Federal Circuit Case Records
    tags:
      - Federal Courts
      - Case Records
      - Legal
    humanURL: https://www.cafc.uscourts.gov/home/case-information/case-records/
    properties:
      - url: https://www.cafc.uscourts.gov/home/case-information/case-records/
        type: Documentation
      - url: https://www.cafc.uscourts.gov/home/case-information/
        type: GettingStarted
      - url: https://raw.githubusercontent.com/api-evangelist/us-court-of-appeals-for-the-federal-circuit/refs/heads/main/json-schema/cafc-case-schema.json
        type: JSONSchema
        title: Federal Circuit Case Schema
      - url: https://raw.githubusercontent.com/api-evangelist/us-court-of-appeals-for-the-federal-circuit/refs/heads/main/json-schema/cafc-opinion-schema.json
        type: JSONSchema
        title: Federal Circuit Opinion Schema
      - url: https://raw.githubusercontent.com/api-evangelist/us-court-of-appeals-for-the-federal-circuit/refs/heads/main/json-schema/cafc-docket-entry-schema.json
        type: JSONSchema
        title: PACER Docket Entry Schema
    description: Case information and records for the U.S. Court of Appeals for the Federal Circuit. Cases filed on or after March 1, 2012, are available through PACER or at public terminals in the Clerk's Office. The court provides aggregated case statistics via a data request process.
name: US Court of Appeals for the Federal Circuit
tags:
  - Federal Government
  - Legal
  - Patent Law
  - Federal Courts
  - Appellate Courts
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-25'
modified: '2026-05-03'
position: Consumer
description: The US Court of Appeals for the Federal Circuit is a federal appellate court with nationwide jurisdiction over cases involving patent law, international trade, government contracts, federal employment, veterans' benefits, and other specialized areas of federal law. The court provides public access to opinions and orders online from 2004 to present, with full case records accessible via PACER for cases filed after March 1, 2012. The PACER system offers developer APIs including the Authentication API and the Case Locator (PCL) API for programmatic access to federal case data across all federal courts.
common:
  - type: Website
    url: https://www.cafc.uscourts.gov/
  - type: Documentation
    url: https://www.cafc.uscourts.gov/home/case-information/
    title: Case Information
  - type: Documentation
    url: https://www.cafc.uscourts.gov/home/case-information/opinions-orders/
    title: Opinions and Orders
  - type: GettingStarted
    url: https://pacer.uscourts.gov/
    title: PACER Registration
  - type: APIReference
    url: https://pacer.uscourts.gov/file-case/developer-resources
    title: PACER Developer Resources
  - type: Documentation
    url: https://www.cafc.uscourts.gov/home/rules-procedures/
    title: Rules and Procedures
  - type: Contact
    url: https://www.cafc.uscourts.gov/home/about-the-court/contact/
    title: Contact the Court
  - type: Features
    data:
      - name: PACER Case Locator API
        description: Programmatic access to the nationwide federal court case index via the PACER Case Locator (PCL) API, enabling searches for cases and associated parties across all federal courts including the Federal Circuit.
      - name: PACER Authentication API
        description: API allowing automated authentication to PACER without a user interface, enabling programmatic access to court records using PACER credentials.
      - name: CM/ECF Electronic Filing
        description: Court's electronic filing system (CM/ECF) for filing and managing case documents. Provides XML tags and NextGen CM/ECF integration.
      - name: Online Opinions and Orders
        description: Free public access to all Federal Circuit opinions, orders, and judgments published from October 2004 to present in PDF format.
      - name: Scheduled Cases Calendar
        description: Online calendar of scheduled oral argument cases and courtroom assignments at the Federal Circuit.
      - name: Statistical Reports
        description: Aggregated case statistics and reports available through the court's media and public information pages, plus data request process.
  - type: UseCases
    data:
      - name: Patent Case Legal Research
        description: Researching Federal Circuit patent law precedent using published opinions, orders, and PACER case dockets.
      - name: Federal Employment and Veterans Claims Research
        description: Finding Federal Circuit decisions on government contracts, federal employment, veterans benefits, and specialized federal jurisdiction.
      - name: Court Records Access via PACER
        description: Programmatic access to Federal Circuit case dockets, filings, and documents using the PACER Authentication API and Case Locator API.
      - name: Appellate Monitoring
        description: Monitoring active Federal Circuit cases, oral arguments, and new opinions relevant to specific technology, trade, or legal areas.
      - name: Legal Data Analytics
        description: Using PACER data to analyze trends in Federal Circuit patent, trade, and government contract decisions for legal research.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/us-court-of-appeals-for-the-federal-circuit/refs/heads/main/vocabulary/us-court-of-appeals-for-the-federal-circuit-vocabulary.yml
    title: US Court of Appeals for the Federal Circuit Vocabulary
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/us-court-of-appeals-for-the-federal-circuit/refs/heads/main/json-ld/us-court-of-appeals-for-the-federal-circuit-context.jsonld
    title: US Court of Appeals for the Federal Circuit JSON-LD Context
  - type: Integrations
    data:
      - name: PACER System
        description: Federal Circuit case records fully integrated with the nationwide PACER federal court records system and CM/ECF filing system.
      - name: CourtListener
        description: Free Law Project's CourtListener provides API access to Federal Circuit opinions and RECAP-archived PACER documents.
      - name: Justia Dockets
        description: Justia aggregates Federal Circuit case docket information and provides public access to filings.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
