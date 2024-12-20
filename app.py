import os
from PIL import Image
import rembg

def convert_images_to_png(directory):
    """
    Converte todas as imagens de um diretório para o formato PNG.

    Args:
        directory (str): Caminho para o diretório contendo as imagens.
    """
    # Verificar se o diretório existe
    if not os.path.exists(directory):
        print(f"O diretório '{directory}' não existe.")
        return

    # Criar um diretório para salvar as imagens convertidas
    output_dir = os.path.join(directory, "converted")
    os.makedirs(output_dir, exist_ok=True)

    # Percorrer os arquivos no diretório
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Verificar se o arquivo é uma imagem
        if not os.path.isfile(filepath):
            continue

        try:
            with Image.open(filepath) as img:
                # Converter para RGB (caso necessário) e salvar como PNG
                output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".png")
                img = img.convert("RGB")
                img.save(output_path, "PNG")
                print(f"Imagem '{filename}' convertida para '{output_path}'.")
        except Exception as e:
            print(f"Erro ao processar o arquivo '{filename}': {e}")

def remove_background_from_images(directory):
    """
    Remove o fundo de todas as imagens em um diretório.

    Args:
        directory (str): Caminho para o diretório contendo as imagens.
    """
    # Verificar se o diretório existe
    if not os.path.exists(directory):
        print(f"O diretório '{directory}' não existe.")
        return

    # Criar um diretório para salvar as imagens sem fundo
    output_dir = os.path.join(directory, "no_background")
    os.makedirs(output_dir, exist_ok=True)

    # Percorrer os arquivos no diretório
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Verificar se o arquivo é uma imagem
        if not os.path.isfile(filepath) or not filename.lower().endswith('.png'):
            continue

        try:
            with open(filepath, "rb") as img_file:
                input_image = img_file.read()
                output_image = rembg.remove(input_image)
                output_path = os.path.join(output_dir, filename)
                with open(output_path, "wb") as out_file:
                    out_file.write(output_image)
                print(f"Fundo removido para a imagem '{filename}' e salvo em '{output_path}'.")
        except Exception as e:
            print(f"Erro ao processar o arquivo '{filename}': {e}")

def resize_images(directory, target_height):
    """
    Redimensiona todas as imagens em um diretório para uma altura específica, mantendo a proporção.

    Args:
        directory (str): Caminho para o diretório contendo as imagens.
        target_height (int): Altura desejada em pixels.
    """
    # Verificar se o diretório existe
    if not os.path.exists(directory):
        print(f"O diretório '{directory}' não existe.")
        return

    # Criar um diretório para salvar as imagens redimensionadas
    output_dir = os.path.join(directory, "resized")
    os.makedirs(output_dir, exist_ok=True)

    # Percorrer os arquivos no diretório
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Verificar se o arquivo é uma imagem
        if not os.path.isfile(filepath) or not filename.lower().endswith('.png'):
            continue

        try:
            with Image.open(filepath) as img:
                # Calcular nova largura mantendo a proporção
                aspect_ratio = img.width / img.height
                target_width = int(target_height * aspect_ratio)
                resized_img = img.resize((target_width, target_height))
                output_path = os.path.join(output_dir, filename)
                resized_img.save(output_path)
                print(f"Imagem '{filename}' redimensionada para '{output_path}'.")
        except Exception as e:
            print(f"Erro ao processar o arquivo '{filename}': {e}")

if __name__ == "__main__":
    # Caminho para o diretório com as imagens
    directory = r"C:\Users\David\Desktop\Projetos Py\img_winnikes\img"
    convert_images_to_png(directory)
    converted_directory = os.path.join(directory, "converted")
    remove_background_from_images(converted_directory)
    no_background_directory = os.path.join(converted_directory, "no_background")
    resize_images(no_background_directory, 700)
