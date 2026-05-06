---
aid: central-intelligence-agency
url: https://raw.githubusercontent.com/api-evangelist/central-intelligence-agency/refs/heads/main/apis.yml
name: Central Intelligence Agency
tags:
  - Federal Government
  - FOIA
  - Government
  - Intelligence
  - National Security
  - Open Data
  - World Factbook
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: The Central Intelligence Agency (CIA) is the United States' civilian foreign intelligence service of the federal government, tasked with gathering, processing, and analyzing national security information from around the world. While the CIA does not maintain a formal public developer program, it publishes a small number of digital resources of interest to civic technologists and researchers, including the CIA.gov public website, the FOIA Electronic Reading Room (CREST) of declassified records, the World Factbook country profiles (open dataset, public domain), the CIA Museum digital collection, the Studies in Intelligence journal archive, and the agency's careers portal. Note that the World Factbook web product was discontinued on 4 February 2026, but a CC0-licensed JSON dataset of all 260 Factbook entities is preserved on GitHub by the community.
apis:
  - aid: central-intelligence-agency:cia-website
    name: CIA Public Website
    tags:
      - Federal Government
      - Intelligence
      - News
    humanURL: https://www.cia.gov/
    properties:
      - url: https://www.cia.gov/
        type: Website
      - url: https://www.cia.gov/about/
        type: About
      - url: https://www.cia.gov/stories/
        type: News
    description: The CIA's primary public-facing website at cia.gov hosts agency news stories, leadership biographies, mission statements, careers and recruiting information, and links to all other public CIA digital properties.
  - aid: central-intelligence-agency:cia-foia-reading-room
    name: CIA FOIA Electronic Reading Room (CREST)
    tags:
      - Declassified
      - Documents
      - FOIA
      - Records Search
      - Transparency
    humanURL: https://www.cia.gov/readingroom/
    properties:
      - url: https://www.cia.gov/readingroom/
        type: Website
      - url: https://www.cia.gov/readingroom/search/site
        type: Search
      - url: https://www.cia.gov/readingroom/collections
        type: Collections
    description: The CIA's FOIA Electronic Reading Room (CREST - CIA Records Search Tool) is a publicly searchable interface to declassified CIA records released under the Freedom of Information Act. The site provides full-text search, document downloads, and curated topical collections suitable for researchers and historians.
  - aid: central-intelligence-agency:cia-world-factbook
    name: CIA World Factbook (Country Profiles)
    tags:
      - Country Profiles
      - Demographics
      - Geography
      - Open Data
      - Reference
      - World Factbook
    humanURL: https://www.cia.gov/the-world-factbook/
    properties:
      - url: https://www.cia.gov/the-world-factbook/
        type: Website
      - url: https://github.com/factbook/factbook.json
        type: OpenData
      - url: https://github.com/factbook/factbook.json
        type: GitHubRepository
    description: The CIA World Factbook is the long-running unclassified almanac of reference information on 260 world entities including all sovereign countries, dependencies, and oceans, organized into the categories of Geography, People and Society, Environment, Government, Economy, Energy, Communications, Transportation, Military and Security, Space, Terrorism, and Transnational Issues. The web product was discontinued 4 February 2026; the community-maintained `factbook.json` GitHub project preserves a CC0 / public-domain JSON dataset of all entities for programmatic access.
  - aid: central-intelligence-agency:cia-museum
    name: CIA Museum Digital Collection
    tags:
      - Artifacts
      - History
      - Museum
    humanURL: https://www.cia.gov/legacy/museum/
    properties:
      - url: https://www.cia.gov/legacy/museum/
        type: Website
      - url: https://www.cia.gov/legacy/museum/artifacts/
        type: Catalog
    description: The CIA Museum digital collection is the public-facing online catalog of artifacts, exhibits, and stories from the CIA Museum, including historical espionage tools, declassified mission gear, and curated narratives about agency history.
  - aid: central-intelligence-agency:cia-studies-in-intelligence
    name: Studies in Intelligence Journal
    tags:
      - Analysis
      - Intelligence
      - Journal
      - Publications
    humanURL: https://www.cia.gov/resources/csi/studies-in-intelligence/
    properties:
      - url: https://www.cia.gov/resources/csi/studies-in-intelligence/
        type: Website
      - url: https://www.cia.gov/resources/csi/
        type: CSI
    description: Studies in Intelligence is the CIA's professional journal published by the Center for the Study of Intelligence (CSI). The site provides unclassified articles, book reviews, and historical analyses on the intelligence profession in PDF and HTML formats.
  - aid: central-intelligence-agency:cia-careers
    name: CIA Careers Portal
    tags:
      - Careers
      - Hiring
      - Jobs
    humanURL: https://www.cia.gov/careers/
    properties:
      - url: https://www.cia.gov/careers/
        type: Website
      - url: https://www.cia.gov/careers/jobs/
        type: Jobs
    description: The CIA Careers portal is the agency's public recruiting site, listing open positions across analysis, operations, science and technology, digital innovation, and support functions, along with eligibility, hiring process, and student/internship program information.
common:
  - type: Website
    url: https://www.cia.gov/
  - type: About
    url: https://www.cia.gov/about/
  - type: News
    url: https://www.cia.gov/stories/
  - type: FOIA
    url: https://www.cia.gov/readingroom/
  - type: WorldFactbook
    url: https://www.cia.gov/the-world-factbook/
  - type: Museum
    url: https://www.cia.gov/legacy/museum/
  - type: Careers
    url: https://www.cia.gov/careers/
  - type: Contact
    url: https://www.cia.gov/contact-cia/
  - type: Privacy Policy
    url: https://www.cia.gov/privacy-statement/
  - type: NoFearAct
    url: https://www.cia.gov/no-fear-act/
  - type: AccessibilityStatement
    url: https://www.cia.gov/accessibility/
  - type: Tor
    url: http://ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion/
  - name: ProgramAreas
    type: ProgramAreas
    data:
      - name: Foreign Intelligence Collection
      - name: All-Source Analysis
      - name: Covert Action
      - name: Counterintelligence
      - name: Counterterrorism
      - name: Cybersecurity
      - name: Science and Technology
      - name: Open-Source Intelligence (OSINT)
  - name: PublicResources
    type: PublicResources
    data:
      - name: World Factbook (Discontinued)
      - name: FOIA Electronic Reading Room (CREST)
      - name: CIA Museum
      - name: Studies in Intelligence Journal
      - name: News and Stories
      - name: Careers Portal
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
