---
layout: page
title: Indic Handwritten Text Recognition
description: Transformer-based OCR (PARSeq) for handwritten text across ten Indic scripts, boosted by transfer learning from printed text.
img: assets/img/indic-htr-teaser.png
importance: 1
category: research
related_publications: true
redirect: https://lalithaevani.github.io/Indic-HTR-CVIP-2024-page/
---

**Problem.** Handwritten Text Recognition (HTR) is hard even for a single
script — writing styles, noise, and imperfections vary widely. It gets harder
across Indic scripts, which have complex character structures, large
character inventories, and comparatively little labeled data.

**Approach.** We adapt PARSeq — a transformer model originally built for
scene-text recognition — to handwritten text across ten Indic scripts (Hindi,
Bengali, Telugu, Tamil, Gujarati, Gurumukhi, Odia, Kannada, Malayalam, Urdu),
and study how much pre-training on printed text before fine-tuning on
handwritten text helps.

**Results.** PARSeq beats prior CNN–RNN baselines on most of the ten
languages, and transfer learning from printed to handwritten text gives a
further, consistent accuracy boost — published at CVIP 2024
{% cite evani2024indichtr %}.

**Links.** [Project page](https://lalithaevani.github.io/Indic-HTR-CVIP-2024-page/) · [Paper](https://link.springer.com/chapter/10.1007/978-3-031-93688-3_17) · [Code](https://github.com/LalithaEvani/Indic-HTR-CVIP-2024)

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/indic-htr-teaser.png" title="India map by script" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  The ten Indic scripts evaluated, and the states where each is dominantly used.
</div>
