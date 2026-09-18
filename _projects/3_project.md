---
layout: page
title: Medical Document Summarization
description: Comparing T5, BART, and PEGASUS for abstractive summarization of medical research documents.
img: assets/img/textsumm-rouge-chart.png
importance: 3
category: coursework
related_publications: true
---

**Problem.** Many medical research documents don't come with a summary or
abstract, making it hard for researchers to quickly judge relevance without
reading the whole document.

**Approach.** We compare five abstractive summarization models — T5 (small,
base, large), BART, and PEGASUS — on the SUMPUBMED dataset (32,689 PubMed
documents), scored with ROUGE-1/2/L.

**Results.** PEGASUS comes out on top on most metrics (ROUGE-1 recall 0.37,
F1 0.36), with BART close behind. Published at ICAAIC 2023
{% cite evani2023textsumm %}.

**Links.** [Project page](https://lalithaevani.github.io/Text-Summarization-ICAAIC-2023-page/) · [Paper](https://ieeexplore.ieee.org/abstract/document/10140885/)

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/textsumm-rouge-chart.png" title="ROUGE performance metrics" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  ROUGE-1/2/L recall, precision, and F1 across T5 (small/base/large), BART, and PEGASUS.
</div>
