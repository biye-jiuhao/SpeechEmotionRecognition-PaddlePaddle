import paddle
import paddle.nn as nn


class Model(nn.Layer):
    def __init__(self, num_class):
        super(Model, self).__init__()
        self.fc0 = nn.Linear(in_features=312, out_features=256)
        self.lstm = nn.LSTM(input_size=256, hidden_size=256, direction='forward')
        self.tanh = nn.Tanh()
        self.dropout = nn.Dropout(p=0.5)
        self.fc1 = nn.Linear(in_features=256, out_features=256)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(in_features=256, out_features=num_class)

    def forward(self, x):
        x = self.fc0(x)
        x = x.reshape((x.shape[0], 1, x.shape[1]))
        y, (h, c) = self.lstm(x)
        x = y.squeeze(axis=1)
        x = self.tanh(x)
        x = self.dropout(x)
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.fc2(x)
        return x