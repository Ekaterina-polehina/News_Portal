from django import template
#from django.template.defaultfilters import stringfilter

register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
#stringfilter

def censor(text):
    #if type(text) is not str:
        #raise ValueError("Фильтр цензурирования применяется только к переменным строкового типа")

    spl_text = text.split()
    # составляем список нецензурных слов.
    explicitwords = ['дВижения',
                     'ТраСсе',
                     'производственных',
                     'Однако',
                     'детонациЮ']

    for ex_word in explicitwords:
        # Остальные буквы цензурируемых слов текста могут быть только в нижнем регистре, поэтому переводим слова списка
        # нецензурных слов в нижний регистр, а первую букву - в верхний.
        ex_word = ex_word.title()

        for word in spl_text:
            # Все слова, которые нужно цензурировать, начинаются с верхнего или нижнего регистра, поэтому переводим первые
            # буквы всех слов текста в верхний регистр.
            word1 = word[0].upper() + word[1:]

            if word1 == ex_word:
                # Например, если мы считаем слово «редиска» ругательством, то из предложения «Нехороший человек — редиска!»
                # после применения фильтра должно получиться «Нехороший человек — р******!»
                text = text.replace(word, word[0] + '*' * (len(word) - 1))


    """Removes all values of arg from the given string"""
    return text
