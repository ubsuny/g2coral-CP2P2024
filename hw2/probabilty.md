1. **Gaussian (Normal) Distribution**:
   - The Gaussian distribution is a continuous probability distribution characterized by a symmetric, bell-shaped curve. It is defined by two parameters: the mean (μ) and the standard deviation (σ).
   - Most laser beams have an intensity spectrum that follows a Gaussian distribution.
   - The probability density function (PDF) of the Gaussian distribution gives the likelihood of observing a particular value and is governed by the formula:
     $\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) \]$
   - The Gaussian distribution is symmetric around its mean, and approximately 68%, 95%, and 99.7% of the data fall within one, two, and three standard deviations from the mean, respectively.

2. **Poisson Distribution**:
   - The Poisson distribution is a discrete probability distribution that models the number of events occurring in a fixed interval of time or space, assuming a constant rate of occurrence and events happening independently.
   - It is commonly used to model countable events.
   - The distribution is characterized by a single parameter, λ (lambda), which represents the average rate of occurrence. Both the mean and variance of the Poisson distribution are equal to λ.
   - The probability mass function (PMF) of the Poisson distribution gives the probability of observing exactly k events in the interval and is given by:
     $\[ P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!} \]$

3. **Sub-Poissonian Distribution**:
   - A sub-Poissonian distribution occurs when the observed variance is less than what would be expected under a Poisson distribution with the same mean.
   - It can arise due to clustering or inhibition of events, finite-size effects, correlations among events, or measurement artifacts.
   - Examples include situations where events tend to occur in clusters rather than independently, leading to reduced variability in event counts.

4. **Super-Poissonian Distribution**:
   - A super-Poissonian distribution occurs when the observed variance is greater than what would be expected under a Poisson distribution with the same mean.
   - It can arise due to clustering or aggregation of events, interactions among events, or measurement artifacts.
   - Examples include scenarios where events exhibit clustering behavior, positive feedback mechanisms lead to increased event occurrence or measurement noise overestimates variability.

These distributions play crucial roles in quantum optics, providing models for understanding and analyzing various phenomena related to the behavior of light and photons.

5. **Photon Statistics**:
   - Coherent Light follows a Poissonian Distribution. Furthermore, it shows good spatial and temporal coherence. This means that the phase of the wave remains constant at all points in space and time.
   - Chaotic Light, also known as partially coherent light, incoherent, or thermal light, follows a Super-Poissonian distribution. In addition, its intensity varies over time. A common source of chaotic light is black body radiation.
   - Quantum Light follows a Sub-Poissonian distribution which is narrower than a Poisson distribution with the same mean. The most striking characteristic of quantum light is that photons arrive at the detector one at a time, with a fixed time between their arrival.
