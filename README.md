# ntpy

مكتبة Python بسيطة لأساسيات نظرية الأعداد وعمليات حسابية مفيدة.

الهدف
------
ntpy تهدف إلى تقديم أدوات سهلة الاستخدام للتعامل مع: الأعداد الأولية، تحليل العوامل، القواسم، دالة أويلر (phi)، دالة موبيوس، ونظرية الباقي الصينية (CRT).

الميزات
-------
- توليد الأعداد الأولية
- اختبار أولية العدد (Miller–Rabin)
- تحليل عدد إلى عوامله الأولية
- استخراج العوامل الأولية
- حساب القواسم، عدد القواسم، ومجموع القواسم
- دالة أويلر (euler_phi)
- دالة موبيوس (mobius)
- حل أنظمة البواقي باستخدام CRT

التثبيت
--------
يمكن تثبيت النسخة الحالية مباشرة من GitHub:

```bash
pip install git+https://github.com/Mustafa200215/ntpy.git
```

أو استنساخ المستودع وتثبيته مح��يًا:

```bash
git clone https://github.com/Mustafa200215/ntpy.git
cd ntpy
pip install .
```

البدء السريع — أمثلة استخدام
---------------------------

```python
import ntpy

# اختبار أولية
print(ntpy.is_prime(17))          # True

# توليد أولية حتى حد
print(ntpy.generate_primes(20))   # [2, 3, 5, 7, 11, 13, 17, 19]

# تحليل العوامل
print(ntpy.factorize(360))       # {2: 3, 3: 2, 5: 1}
print(ntpy.prime_factorize(360)) # [2, 3, 5]

# القواسم
print(ntpy.divisors(12))         # [1, 2, 3, 4, 6, 12]
print(ntpy.num_divisors(12))     # 6
print(ntpy.sum_divisors(12))     # 28

# دالة أويلر وموبيوس
print(ntpy.euler_phi(10))        # 4
print(ntpy.mobius(30))           # -1

# Chinese Remainder Theorem
modulus, solution = ntpy.crt([3, 5], [2, 3])
print(modulus, solution)         # (15, 8)  => x ≡ 8 (mod 15)
```

ملاحظات وقيود
-------------
- دوال المكتبة مناسبة للأعداد الصحيحة الصغيرة والمتوسطة. لبعض الوظائف (مثل تحليل الأعداد الكبيرة جدًا) قد تحتاج خوارزميات أسرع (مثلاً Pollard Rho).
- is_prime تستخدم اختبار Miller–Rabin بعدد افتراضي من الجولات؛ يمكن تعديل عدد الجولات عبر الوسيط `k` لزيادة الثقة.

تنمية واختبار
--------------
المشروع يحتوي على مجلد `tests/` مع اختبارات بوحدة `pytest`. لتشغيل الاختبارات محليًا:

```bash
pip install -r requirements.txt   # إن وُجد
pytest -q
```

اقتراحات لتحسين المستودع
------------------------
- إضافة نوعية المعطيات (type hints) و docstrings لكل دالة.
- تحسين is_prime لاستخدام قواعد حتمية (deterministic bases) لما يصل إلى 64-bit إن أمكن.
- إضافة Pollard's Rho لتحسين تحليل الأعداد الكبيرة.
- إضافة CI (GitHub Actions) لتشغيل الاختبارات والتحقق من تنسيق الكود (black, flake8, mypy).

المساهمة
--------
مرحب بالمساهمات! الرجاء فتح Issue أو Pull Request. قد تفيد إضافة ملف CONTRIBUTING.md لتوضيح إرشادات المساهمة.

الرخصة
------
المشروع مرخّص بموجب رخصة MIT — انظر ملف LICENSE.

المؤلف
------
Mustafa Hato (MHD)

رابط المشروع
-------------
https://github.com/Mustafa200215/ntpy
