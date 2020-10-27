import yaml


def read_yaml(file):
    """读取 yaml 文件"""
    with open(file, encoding='utf8') as f:
        conf = yaml.load(f, Loader=yaml.SafeLoader)
    return conf


def write_yaml(file, data):
    with open(file, 'w', encoding='utf8') as f:
        yaml.dump(data, f)


if __name__ == '__main__':
    print(read_yaml("./../config/config.yml"))
