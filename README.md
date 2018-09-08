# genocide_emotions
Emotions recognition net art project

Proyecto reconocimiento de emociones sobre el rostro de Miguel Etchecolatz durante un video de uno de los juicios por genocidio.


OBJETIVOS
  A partir del procesamiento de un fotograma con el rostro de Miguel Etchecolatz de un video de los juicios en los que fue condenado por crímenes contra la humanidad y utilizando un sistema de inteligencia artificial de reconocimiento de emociones, el sitio se propone generar por comparación analogías y metáforas que aporten otros elementos a la reflexión sobre el genocidio argentino ocurrido a partir de 1976. Los valores de comparación surgen de la consulta en motores de búsqueda de las palabras ingresadas por los visitantes. Las imágenes resultantes de dicha búsqueda son procesadas con el mismo algoritmo y organizadas por proximidad de resultados con el fotograma de referencia. 
  Se espera que las palabras de búsqueda y los apodos elegidos por los participantes agreguen a su vez  otro nivel de significación.
  

MEMORIA DESCRIPTIVA
  El 20 de agosto pasado, a los 95 años, falleció María Isabel Chorobik de Mariani, una de las fundadoras de Abuelas de Plaza de Mayo y abuela de Clara Anahí Mariani. Clara Anahí fue secuestrada el 24 de noviembre de 1976 a los 3 meses de edad y continúa desaparecida. Desde entonces y hasta su muerte Chicha de Mariani nunca dejó de buscar a su nieta y de perseguir Justicia por los crímenes genocidas de la dictadura.
  Entre las imágenes reproducidas durante ese día, una en particular, un pequeño fragmento donde se ve el rostro de Miguel Etchecolatz, me produjo un profundo sentimiento de espanto. Él fue quien estuvo a cargo del operativo de la casa de calle 30, en la ciudad de la Plata en el que fue asesinada  la madre de Clara Anahí junto a otros 4 jóvenes, militantes de Montoneros. Los restos de esa casa se conservan como espacio de memoria  y testimonio. 


 Hoy, que más de 500 genocidas condenados han sido beneficiados con prisión domiciliaria, y la historia del genocidio argentino se sigue escribiendo, reflexionar sobre lo sucedido, sobre quienes fueron sus ejecutores como Etchecolatz, sobre quienes fueron sus impulsores y beneficiarios,  la consigna de Memoria, Verdad y Justicia se vuelve más urgente. Y es en esa urgencia que se inscribe este proyecto.

DESCRIPCIÓN TÉCNICA
   A partir de un  un fotograma de un video y utilizando algoritmos de visión computacional e inteligencia artificial (machine learning) se obtienen una serie de valores relacionados a las emociones inferidas en el rostro presente en el fotograma. Estos valores se sobreimprimen en el video.
A su vez se presenta al usuario una interfaz de búsqueda que genera una consulta en un motor de búsqueda dando como resultado una colección de imágenes. Sobre estas imágenes se ejecuta un proceso de reconocimiento de rostros y se obtiene un coeficiente de emociones que será comparado con el fotograma de referencia.


PROYECTOS DE REFERENCIA
Artificial emotions (Gustavo Romano, 2018): http://4rt.eu/ae/


URLS VIDEOS
Historias debidas Chicha Mariani(Canal Encuentro) https://www.youtube.com/watch?v=t50mBcqlxuk
Infojus, lectura de condena a cadena perpetua La Cacha https://www.youtube.com/watch?v=R9SoHnxQxZ8
Historias debidas Chicha Mariani(Canal Encuentro) https://www.youtube.com/watch?v=t50mBcqlxuk
Lectura de condena a Etchecolatz (Televisión Pública Argentina, 2006) https://www.youtube.com/watch?v=wG4RWOUG_jQ
Argentinos repudian cambio de sentencia al genocida Miguel Etchecolatz (teleSur TV,2017): https://www.youtube.com/watch?v=SACD0owgvS4

URLS TÉCNICAS
OpenCV (Open source computer vision library) https://opencv.org/
Tensorflow (Machine learning framework) https://www.tensorflow.org/
Qwant search engine https://api.qwant.com

DESCRIPCIÓN TÉCNICA
Sitio desarrollado en Python/Django con base de datos Sqlite. Procesamiento de imágenes con OpenCV, obtención de coeficiente de emociones Tensorflow.
La URL de despliegue todavía no está disponible.
	
RECONOCIMIENTOS
The artificial emotions curator http://4rt.eu/ae/index.html - Gustavo Romano (gusrom@gmail.com)
Emotion detection project by Atul Balaji https://github.com/atulapra/Emotion-detection

LICENCIA
GPL v3.0 https://www.gnu.org/licenses/gpl-3.0.en.htm


Victor Pesquin
vpesquin@acm.org
Buenos Aires, 6 de septiembre 2018
